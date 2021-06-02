# Python library that detects duplicate files

It has two modes: Fast and Hashed (slower, obviously):

- Fast mode called by the function: get_repeated_fast(directory) compares similar files by their name.
- Hashed mode called by the function: get_repeated(directory) compares files by hashing them.
Standart algorithm is md5 but it may be changed with the optional parameter mode. (Default would be mode="md5").

There to more functions: 
- remove: Removes duplicates.
- move: Moves duplicates to a specified folder.


## Quick test:
Quick test may be done calling make from the command line. This checks that similar files actually have the same size. Some sort of sanity check.

## WIP: A lot.
