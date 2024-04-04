##///////////////////// PROBLEM STATEMENT /////////////////////
## Given an int list, print True if it contains a 2 or a 3.  //
##    2, 5  -> True                                          //
##    4, 3  -> True                                          //
##    4, 5  -> False                                         //
##/////////////////////////////////////////////////////////////


def find(l):
    for i in l:
        if i == 2 or i == 3:
            return True
    return False

list = [1, 4, 1, 1]
print(find(list))
