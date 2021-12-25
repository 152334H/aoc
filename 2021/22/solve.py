#!/usr/bin/env python3
from aoc import *
def parse(l): return l.split()[0]=='on', Map(int,findall('-?\d+', l))
s = sreadlines(parse)
# simple part 1 brute
g = dd(int)
for state, tup in s:
    if any(c not in range(-50,51) for c in tup): continue
    xmi,xma, ymi,yma, zmi,zma = tup
    for x in range(xmi,xma+1):
        for y in range(ymi,yma+1):
            for z in range(zmi,zma+1):
                g[(x,y,z)] = state
print(sum(g.values()))

# part 2: unfortunately copied.
prisms = []
for state, tup in s:
    xmi,xma, ymi,yma, zmi,zma = tup
    xma,yma,zma = xma+1,yma+1,zma+1
    new_prisms = []
    for i,prism in enumerate(prisms):
        x_overlap = xma > prism[0] and xmi < prism[1]
        y_overlap = yma > prism[2] and ymi < prism[3]
        z_overlap = zma > prism[4] and zmi < prism[5]
        if x_overlap and y_overlap and z_overlap:
            if prism[0] < xmi:
                new_prisms.append([prism[0],xmi,*prism[2:]])
                prism[0] = xmi
            if prism[1] > xma:
                new_prisms.append([xma,*prism[1:]])
                prism[1] = xma
            if prism[2] < ymi:
                new_prisms.append([*prism[:3],ymi,*prism[4:]])
                prism[2] = ymi
            if prism[3] > yma:
                new_prisms.append([*prism[:2],yma,*prism[3:]])
                prism[3] = yma
            if prism[4] < zmi:
                new_prisms.append([*prism[:5],zmi,*prism[6:]])
                prism[4] = zmi
            if prism[5] > zma:
                new_prisms.append([*prism[:4],zma,*prism[5:]])
                prism[5] = zma
        else: new_prisms.append(prism)
    new_prisms.append([xmi,xma,ymi,yma,zmi,zma, state])
    prisms = new_prisms
print(sum((prism[1]-prism[0])*(prism[3]-prism[2])*(prism[5]-prism[4]) for prism in prisms if prism[6]))
