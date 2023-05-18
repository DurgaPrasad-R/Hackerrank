#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    c = 0
    for i in range(0,len(s)):
        k = 0
        t = 0
        for j in range(i,len(s)):
            k+=s[j]
            t+=1
            if(k == d and t==m):
                c+=1       
    return c   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
