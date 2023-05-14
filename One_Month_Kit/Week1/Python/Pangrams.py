#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    s = s.lower()
    l = list(set([ord(i) for i in s if i!=' ']))
    if len(l) == 26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
