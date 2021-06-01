from glob import glob,iglob
from collections import defaultdict
import os
import hashlib
from tqdm import tqdm



def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    with open(f_path, 'rb') as file:
        data = file.read()
    h.update(data)
    digest = h.hexdigest()
    return digest

#list(iglob(dir_))
"""
Get repeated names
"""
def get_repeated_fast(dir_):
    d = defaultdict(lambda :0)
    for file in iglob(dir_):
        name = file.split("/")[-1]
        d[name]=d[name]+1
    res = []
    for name,number in filter(lambda k:k[1]>1,d.items()):
        res.append(sorted(glob(f"MEGA/ZZZ/*/{name}"),key=os.path.getmtime))
    return res

"""
Get repeated files by hashing algorithm
Default hash is md5
"""
def get_reapeated(dir,mode="md5"):
    d = defaultdict(lambda :[0,[]])
    for file in tqdm(glob(dir_)):
        #name = file.split("/")[-1]
        h=get_hash(file,mode=mode)
        #print(d[h][0])
        d[h][0]=d[h][0]+1
        d[h][1].append(file)
    res = []
    for hash_,list_ in filter(lambda k:k[1][0]>1,d.items()):
        res.append(sorted(list_[1],key=os.path.getmtime))
    return res

"""
Calculates the difference between hashing
and fast checking (which just checks file names)
"""
def diff(dir_):
    diff=[]
    res = get_repeated_fast(dir_)
    res2 = get_repeated(dir_)
    for i in res2:
        el = i[0]
        flag = False
        for j in res:
            if el in j:
                flag = True
                break
        if not flag:
            diff.append(el)
    return diff

"""
Get all files that match a particular file
"""
def find_matches(match,dir_,list_):
    list_ = get_repeated(dir_)
    return list(filter(lambda x: match in x, list_))



"""
Calculates saved space
"""
def check_saves(list_):
    mbs = 0
    for els in list_:
        mbs = mbs + os.path.getsize(els[0])*(len(els)-1)/1024**2
    print(f"Saved {mbs/1024} gbs")
    return mbs

"""
Removes duplicate files, except for the oldest file
"""
def remove(list_):
    for els in list_:
        for i in range(1,len(els)):
            os.remove(els[i])

"""
Moves duplicate files to a specified folder, except for the oldest file
"""
def remove(list_,dest):
    for els in list_:
        for i in range(1,len(els)):
            name = els[i].split("/")[-1]
            os.rename(els[i],f"{dest}/{name}")

dir_="MEGA/ZZZ/*/*.gif"
