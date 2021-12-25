#!/usr/bin/env python3
from aoc import *
inp = sreadlinelines(div='\n')
s = [[tuple(int(v) for v in s.split(',')) for s in scan[1:]] for scan in inp]

def reorient(origin_scan, distant_scan):
    planes = [set() for _ in range(3)]
    for coords in origin_scan:
        for i,c in enumerate(coords): planes[i].add(c)
    
    tie = {}
    for axis in range(3):
        for sign in [1,-1]:
            for i in range(-2000,2000):
                test = set(sign*p[axis]-i for p in distant_scan)
                for main_ax,ax in enumerate(planes):
                    if len(test & ax) >= 11: #NOTE: not 12 because sets
                        tie[axis] = (main_ax,sign,-i)
                        #break
    if len(tie) != 3: return None
    print(tie)
    #
    real_pos = [None]*3
    for cur_ax,(main_ax,sign,i) in enumerate(tie.values()):
        real_pos[main_ax] = i
    #
    real_points = []
    for p in distant_scan:
        new_p = [None]*3
        for cur_ax,v in enumerate(p):
            main_ax,sign,i = tie[cur_ax]
            new_p[main_ax] = sign*v #sign*v+i
        real_points.append(tuple(new_p))
    return real_pos, real_points

seen = set([0])
world = set(p for p in s[0])
border = [0]
scanners = [None for _ in range(len(s))]
scanners[0] = (0,0,0)
while border:
    nb = []
    for left_i in border:
        for i in range(len(s)):
            if i in seen: continue
            res = reorient(s[left_i],s[i])
            if res is not None:
                seen.add(i)
                nb.append(i)
                relative_pos, relative_points = res
                #
                s[i] = relative_points
                real_pos = tuple(relative_pos[j]+scanners[left_i][j] for j in range(3))
                scanners[i] = real_pos
                #
                real_points = [tuple(p[j]+real_pos[j] for j in range(3)) for p in relative_points]
                world.update(real_points)
    border = nb

ma = 0
for a,b in combinations(scanners,2):
    ma = max(ma,abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]))
print(len(world))
print(ma)
