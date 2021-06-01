from compose import compose
"""
Tests that everything is okay
"""

from main import *

"""
Missing _dir introduced through command line
"""


list_=get_repeated(_dir)

def equal(l):
    for i in range(1,len(l)):
        if l[0]!=l[i]:
            return False
    return True


print("Checking \"equal\" files have equal size")

lfilter = compose(list,filter)
lmap = compose(list,map)

filtered=lfilter(lambda x : not equal(x),
       [lmap(lambda x: os.path.getsize(x),y) for y in list_])
assert len(filtered)==0
print("Checked")
