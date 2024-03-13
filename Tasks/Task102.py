from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a string length 2 made of its first 2 chars. If the //
## string length is less than 2, use  '@' for the missing chars.             //
##   ("hello") -> "he"                                                       //
##   ("hi") -> "hi"                                                          //
##   ("h") -> "h@"                                                           //
##/////////////////////////////////////////////////////////////////////////////

x = input("string: ")
if len(x) < 2:
    print(x[0]+"@")
else:
    print(x[:2])