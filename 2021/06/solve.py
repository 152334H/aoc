#!/usr/bin/env python3
from aoc import *
s = sread(div=',')
def solve(days: int): 
    state = Counter(map(int,s))
    for day in range(days):
        ns = dd(lambda: 0)
        for k,v in state.items():
            if not k:
                ns[8] += v
                ns[6] += v
            else: ns[k-1] += v
        state = ns
    return sum(ns.values())
for part in (80,256): print(solve(part))
