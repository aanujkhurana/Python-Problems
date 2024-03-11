from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string.                                                      //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////

a = input("")
countcat = 0
countdog = 0
if "cat" in a:
    countcat += 1
if "dog" in a:
    countdog += 1

if countcat == countdog:
    print(True)
else:
    print(False)
