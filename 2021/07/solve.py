#!/usr/bin/env python3
from aoc import *
s = sread(int, div=',')

''' Easily written bruteforce:
def brute(part: bool):
    mi = 999999999999
    for i in range(min(s), max(s)+1):
        res = 0
        for n in s:
            dist = abs(n-i)
            res += dist*(dist+1)//2 if part else dist
        mi = min(mi, res)
    return mi
for i in range(2): print(brute(i))'''

# More efficient:
from numpy import median
mean = sum(s)//len(s)
med = median(s) # not exactly sure that this will be an int
medians = [int(med)] if med % 1 == 0 else [int(med), int(med)+1]
print(min(sum(abs(n-m) for n in s) for m in medians)) # part 1: n-median
print(sum(abs(n-mean)*(abs(n-mean)+1)//2 for n in s)) # part 2: n-mean

