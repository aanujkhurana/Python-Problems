from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a version without the first 2 chars. Except keep    //
## the first char if it is 'a' and keep  the second char if it is 'b'. The   //
## string may be any length.                                                 //
##   "Hello" -> "llo"                                                        //
##   "java" -> "va"                                                          //
##   "away" -> "aay"                                                         //
##/////////////////////////////////////////////////////////////////////////////

def remove(string):
    if len(string) < 2:
        return string
    elif string[0] == 'a' and string[1] == 'b':
        return string
    elif string[0] == 'a':
        return string[0] + string[2:]
    elif string[1] == 'b':
        return string[1:]
    else:
        return string[2:]

string = "HAhele"

print(remove(string))