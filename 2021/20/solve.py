#!/usr/bin/env python3
from aoc import *
enhancer, image = sreadlinelines(div='\n')

enhancer = enhancer[0]
image = Grid(image, default=lambda: '.', oob_behaviour='expand')
def enhance():
    new_def = '#.'[image.default_factory() == '#'] if enhancer[0]=='#' else '.'
    ng = Grid({Point(0,0):'.'}, default=lambda: new_def, oob_behaviour='expand')
    yr = range(image.yrange.start-2, image.yrange.stop+2)
    xr = range(image.xrange.start-2, image.xrange.stop+2)
    for y in yr:
        for x in xr:
            flat = ''.join(image[x+dx, y+dy] for dy in range(-1, 2) for dx in range(-1, 2))
            n = int(flat.replace('#','1').replace('.','0'),2)
            ng[x,y] = enhancer[n]
    return ng
for loop in range(50):
    image = enhance()
    if loop in (1,49): 
        print(sum(1 for c in image.values() if c == '#'))
