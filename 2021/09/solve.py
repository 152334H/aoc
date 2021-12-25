#!/usr/bin/env python3
from aoc import *
g = Grid(sreadlines(lambda l: [int(c) for c in l]), forbidden=[9])

# part 1: iterate through all points p to find where all(g[adj_c] > g[p])
print(sum(g[p]+1 for p in g\
        if all(g[oth] > g[p] for oth in g.adj(p))))

# part 2: flood fill everything (borders are '9'), and
# get the product of the sizes of the 3 largest pools
seen = set()
sizes = []
for p in g:
    if p in seen: continue
    d_map = g.distance_map(p)
    sizes.append(len(d_map))
    seen |= d_map.keys()

sizes.sort()
print(prod(sizes[-3:]))
