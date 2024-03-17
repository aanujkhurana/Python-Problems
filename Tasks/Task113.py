from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if the first 2 chars in the string also appear //
## at the end of the string, such as with "edited".                          //
##   "edited" -> True                                                        //
##   "edit" -> False                                                         //
##   "ed" -> True                                                            //
##/////////////////////////////////////////////////////////////////////////////

x=input()
if len(x) <= 2:
    print(True)
elif x[:2]==x[-2:]:
    print(True)
else:
    print(False)