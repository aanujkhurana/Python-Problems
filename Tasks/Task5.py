from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the strings are different lengths, omit     //
## chars from the longer string so it is the same length as the shorter      //
## string. So "Hello" and "Hi" yield "loHi". The strings may be any length.  //
##                                                                           //
##   "Hello", "Hi" -> "loHi"                                                 //
##   "Hello", "java" -> "ellojava"                                           //
##   "java", "Hello" -> "javaello"                                           //
##/////////////////////////////////////////////////////////////////////////////
a = input("")
b = input("")
if len(a) > len(b):
    a = a[len(b)+1:]
    print(a + b)
if len(a) < len(b):
    b = b[len(a)+1:]
    print(a + b)