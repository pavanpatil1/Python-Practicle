#!/bin/python

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def solve(year):

    if (year == 1918):
        print '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        print '12.09.%s' %year
    else:
        print '13.09.%s' %year
    

if __name__ == '__main__':


    year = int(raw_input().strip())

    result = solve(year)

