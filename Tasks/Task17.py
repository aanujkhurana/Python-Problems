from PyTest import *
##///////////////// PROBLEM STATEMENT /////////////////////
## Given a list of ints, print True if there is a        //
## 1 in the list with a 2 somewhere later in the list.   //
##    1, 3, 2  -> True                                   //
##    3, 1, 2  -> True                                   //
##    3, 1, 4, 5, 2  -> True                             //
##/////////////////////////////////////////////////////////



def check(lst):
    if 1 in lst and 2 in lst[lst.index(1):]:
        return True
    return False
