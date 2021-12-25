#!/usr/bin/env python3
from aoc import *
g = Grid(sreadlines(lambda l: [int(c) for c in l]))

flashes = 0
for step in range(999999):
    if step == 100: print(flashes)
    for p in g: g[p] += 1
    seen = set()
    def inner(p) -> None:
        for oth in g.adj8(p): g[oth] += 1
        g[p] = -99999
        seen.add(p)
    while (add := sum(not inner(p) for p in g if g[p] > 9)): flashes += add
    if len(seen) == len(g): break # note: breaks part 1 if step < 100
    for p in seen: g[p] = 0

print(step+1)
