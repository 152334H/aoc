#!/usr/bin/env python3
from aoc import *
s = sreadlines()

def dijk(g):
    q = PQ([(0,Point(0,0))])
    end = Point(g.xrange.stop-1, g.yrange.stop-1)
    seen = set()
    while q:
        d, p = q.pop()
        if p == end: break
        if p in seen: continue
        seen.add(p)
        for oth in g.adj(p): q.push((d+g[oth], oth))
    print(d)

dijk(Grid([[int(c) for c in l] for l in s]))

# Compressed grid expansion
new_s = [''.join(''.join(str((int(c)+x+y-1)%9 +1) for c in l) for x in range(5))
         for y in range(5) for l in s]
dijk(Grid([[int(c) for c in l] for l in new_s]))
