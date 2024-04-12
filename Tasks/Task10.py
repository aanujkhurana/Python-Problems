from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Start with 2 int lists, a and b. Consider the sum of the values in each   //
## list.  Print the list which has the largest sum. In event of a tie,       //
## print a.                                                                  //
##    1, 2    3, 4  ->  3, 4                                                 //
##    3, 4    1, 2  ->  3, 4                                                 //
##    1, 1    1, 2  ->  1, 2                                                 //
##/////////////////////////////////////////////////////////////////////////////


def largeSum(a,b):
    if sum(a) >= sum(b):
        return a
    else:
        return b
    
a = [1, 2]
b = [3, 4]
print(largeSum(a,b))