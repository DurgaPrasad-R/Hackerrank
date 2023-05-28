#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = s1
    l = s2
    res = ""
    for i in range(k):
        s1 = s1[1:len(s1)]+s1[0]
        s2 = s2[1:len(s1)]+s2[0]
    for i in range(len(s)):
        if s[i] in p or s[i] in l:
            for j in range(len(s1)):
                if(s[i] == p[j]):
                    res+=s1[j]
                if (s[i] == l[j]):
                    res+=s2[j]
        else:
            res+=s[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
