
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if 6 appears as either the first or      //
## last element in the list. The list will be length 1 or more.              //
##    1, 2, 6  -> True                                                       //
##    6, 1, 2, 3  -> True                                                    //
##    3, 2, 1 -> False                                                       //
##/////////////////////////////////////////////////////////////////////////////


def findSix(list):
    if list[0] == 6 or list[-1] == 6:
        return True
    else:
        return False

list = [1,2,3,4,5,6]
print(findSix(list))

