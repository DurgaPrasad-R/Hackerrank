#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    s = 0
    for i in range(32):
        if(n == 0):
            s+=pow(2,i)
        else:
            if(n%2 == 0):
                s+=pow(2,i)
        n = n//2
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
