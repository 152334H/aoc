#!/usr/bin/env python3
from aoc import *
s = sreadlines(div=' ')

def solve(f):
    pos = Point(0,0)
    for (dir, dist) in s:
        pos += f({'up': 'D', 'down': 'U', 'forward': 'R'}[dir], int(dist))
    print(pos.x * pos.y)

solve(lambda d,w: char_to_dir(d)*w)
aim = 0
solve(lambda d,w: Point(w,aim*w) if d=='R' else\
        globals().update(aim=aim+char_to_dir(d).y*w) or Point(0,0)) # None or x == x
