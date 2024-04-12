from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given an int list, if there is a 2 in the list immediately followed by    //
## a 3, set the 3 element to 0. Print the changed list.                      //
##   1, 2, 3 -> 1, 2, 0                                                      //
##   2, 3, 5 -> 2, 0, 5                                                      //
##   1, 2, 1 -> 1, 2, 1                                                      //
##/////////////////////////////////////////////////////////////////////////////


def checkList(lst):
    for i in range(len(lst)-1):
        if lst[i] == 2 and lst[i+1] == 3:
            lst[i+1] = 0
    return lst