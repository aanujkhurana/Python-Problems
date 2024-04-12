from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if the list contains either 3 even or    //
## 3 odd values all next to each other.                                      //
##    2, 1, 3, 5  -  > True                                                  //
##    2, 1, 2, 5  -  > False                                                 //
##    2, 4, 2, 5  -  > True                                                  //
##/////////////////////////////////////////////////////////////////////////////


def check(lst):
    for i in range(len(lst)-2):
        if lst[i]%2 == 0 and lst[i+1]%2 == 0 and lst[i+2]%2 == 0:
            return True
        elif lst[i]%2 != 0 and lst[i+1]%2 != 0 and lst[i+2]%2 != 0:
            return True
    return False