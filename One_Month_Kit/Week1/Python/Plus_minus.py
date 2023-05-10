#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in arr:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print('{p:.6f}\n{n:.6f}\n{z:.6f}'.format(p = p/len(arr),n = n/len(arr),z =z/len(arr)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
