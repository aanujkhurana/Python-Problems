from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if "bad" appears starting at index 0 or 1 in   //
## the string, such as with "badxxx" or  "xbadxx" but not "xxbadxx". The     //
## string may be any length, including 0.                                    //
##   "badxx" -> True                                                         //
##   "xbadxx" -> True                                                        //
##   "xxbadxx" -> False                                                      //
##/////////////////////////////////////////////////////////////////////////////

a = input("")
if a[0:3] == "bad":
    print(True)
elif a[1:4] == "bad":
    print(True)
elif a[-3:] == "bad":
    print(True)
else:
    print(False)