#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
   print(sum(arr)-max(arr),sum(arr)-min(arr))

 
  

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
