#!/usr/bin/env python3
from aoc import *
s = sread()[13:].split(', ')
d = dict(eq.split('=') for eq in s)
ranges = [Map(int,d[c].split('..')) for c in 'xy']
xrange,yrange = [range(t[0],t[1]+1) for t in ranges]

def test(v) -> Optional[int]:
    p = Point(0,0)
    ymax = -9999999999999
    while not (p.x in xrange and p.y in yrange):
        ymax = max(ymax, p.y)
        p += v
        v += Point([-1,1][v.x<0] if v.x else 0, -1)
        if p.y < yrange.start or (not v.x and p.x not in xrange): break
    else: return ymax
    return None

ma = -99999999
cnt = 0
for x in range(int(xrange.start**.5),xrange.stop):
    print('x:',x)
    for y in range(yrange.start,100):
        res = test(Point(x,y))
        if res is not None:
            cnt += 1
            ma = max(ma,res)
print(ma)
print(cnt)
