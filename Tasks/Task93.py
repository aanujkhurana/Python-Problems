from PyTest import *
##/////////////////////// PROBLEM STATEMENT ////////////////////////////
## Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue,. ..6=Sat,  //
## and a boolean indicating if we are on vacation, print a string of  //
## the form "7:00" indicating when the alarm clock should ring.       //
## Weekdays, the alarm should be "7:00" and on the weekend it should  //
## be "10:00". Unless we are on vacation -- then on weekdays it       //
## should be "10:00" and weekends it should be "off".                 //
##   1  False -> 7:00                                                 //
##   0  False -> 10:00                                                //
##   0  True  -> off                                                  //
##   5  True  -> 10:00                                                //
##//////////////////////////////////////////////////////////////////////
