#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    inValley = False
    vallies = 0
    hgt = 0
    
    for step in s:
        if step == 'U':
            hgt += 1
        else:
            hgt -= 1
            
        if not inValley:
            if hgt < 0:
                inValley = True
        elif hgt == 0:
            inValley = False
            vallies += 1
            
    return vallies 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
