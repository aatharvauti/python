#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    # Checking if last two elements of time
    # is AM *and* first two elements are 12
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
          
    # remove the AM    
    elif s[-2:] == "AM":
        return s[:-2]
      
    # Checking if last two elements of time
    # is PM *and* first two elements are 12   
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
          
    else:
        # add 12 to hours and remove PM
        return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
