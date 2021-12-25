#!/usr/bin/env python3
from aoc import *
g = Grid(sreadlines(), oob_behaviour='loop')
for step in range(99999):
    moves = 0
    def rep(x, dp):
        global moves
        ng = Grid(g, oob_behaviour='loop')
        for p,c in g.items():
            if c == x and g[p+dp] == '.':
                ng[p+dp] = x
                ng[p] = '.'
                moves += 1
        return ng
    g = rep('>', Point(1,0))
    g = rep('v', Point(0,1))
    if not moves: break
print(step+1)

