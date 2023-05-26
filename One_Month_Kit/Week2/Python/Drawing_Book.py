#!/bin/python3

import math
import os
import random
import re
import sys


def pageCount(n, p):
    c = 0
    if n/2>=p:
        for i in range(1,p,2):
            c+=1
    else:
        if(n%2 == 0):
            for i in range(n,p,-2):
                c+=1
        else:
            for i in range(n,p,-2):
                if(p+1 == i):
                    continue
                else:
                    c+=1
    return c
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
