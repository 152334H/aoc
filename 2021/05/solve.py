#!/usr/bin/env python3
from aoc import *
s = sreadlines(div=' -> ')
grids = [Grid([[0]], default=lambda: 0, oob_behaviour='expand') for _ in range(2)]
for l in s:
    start,end = (Point(*map(int,t.split(','))) for t in l)
    d = end-start # direction vector
    d //= abs(d.x if d.x else d.y)
    is_straight = bool(d.x and d.y)
    while start != end+d: # include endpoint
        for g in grids[is_straight:]: g[start] += 1
        start += d
for g in grids: print(sum(1 for v in g.values() if v > 1))
