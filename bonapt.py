#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    p  = sum(bill)
    l  = bill[k]
    j = (p - l)/2
    r = b - j
    if(b == j):
        print("Bon Appetit")
    else:
        print(r)

if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)
