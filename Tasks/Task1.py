# from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, print True if either of the strings appears at the     //
## very end of the other string, ignoring upper/lower case differences       //
## (in other words, the computation should not be "case sensitive").         //
##   "Hiabc", "abc" -> True                                                  //
##   "AbC", "HiaBc" -> True                                                  //
##   "abc", "abXabc" -> True                                                 //
##   "abc", "abXaXc" -> False                                                //
##/////////////////////////////////////////////////////////////////////////////
a=input("").upper()
b=input("").upper()
for n in a:
    for j in b:
        if n[::-1] == j[0:]:
            print("yes")
