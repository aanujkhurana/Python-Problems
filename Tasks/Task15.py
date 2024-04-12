from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given an int list, print True if the list contains 2 twice, or 3 twice.   //
## The list will be length 0, 1, or 2.                                       //
##    2, 2  -> True                                                          //
##    3, 3  -> True                                                          //
##    2, 3  -> False                                                         //
##/////////////////////////////////////////////////////////////////////////////


def check(lst):
    if lst.count(2) == 2 or lst.count(3) == 2:
        return True
    return False