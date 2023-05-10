#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    if(s[8:] == 'AM'):
        n = ''
        update = int(s[:2])%12
        n = '0'+str(update)+s[2:8]
        return n
    else:
        n = ''
        update = 12+int(s[:2])%12
        n = str(update)+s[2:8]
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
