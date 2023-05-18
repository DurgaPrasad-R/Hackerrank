#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    s = list(set(ar))
    c = 0
    for i in s:
        c+=ar.count(i)//2
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
