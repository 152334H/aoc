#!/usr/bin/env python3
from aoc import *
dots, folds = sreadlinelines(div='\n')
dots = {Point(*(int(v) for v in l.split(','))):'#' for l in dots}
dots[Point(0,0)] = '.' # ensure xmin|ymin == 0
g = Grid(dots, default=lambda:'.')
folds = [l[11:].split('=') for l in folds]

for i,f in enumerate(folds):
    # fold, assuming all folds are in the exact middle
    typ, line = (f[0]=='y'), int(f[1])
    for p in list(g.keys()):
        d = Point(*[(p[typ]-line)*2,0][::(1,-1)[typ]]) # Great horrors
        if p[typ] > line: g[p-d] = '.#'['#' in (g[p-d], g.pop(p))]
    if typ: g.yrange = range(line)
    else: g.xrange = range(line)
    # part 1:
    if not i: print(sum(1 for v in g.values() if v == '#'))
print(g) # part 2
