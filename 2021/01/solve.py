#!/usr/bin/env python3
from aoc import *
s = sreadlines(int)

def solve(window_size: int):
    return len(Filter(lambda i:
        sum(s[i-1:i+window_size-1]) < sum(s[i:i+window_size]),
        range(1, len(s)-window_size+1)))

print(solve(1))
print(solve(3))
