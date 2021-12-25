#!/usr/bin/env python3
from aoc import *
# template and pair ins rules
head, edges = sreadlinelines(div='\n')
poly = head[0]
edges = [edges.split(' -> ') for edges in edges]
rules = {t[0]:t[1] for t in edges}

def ans_from(d: Dict[str,int]):
    c_count = dd(lambda:0)
    for k,v in d.items():
        for c in k: c_count[c] += v
    # only the two ends of the polymer will NOT be double-counted.
    c_count[poly[0]] += 1
    c_count[poly[-1]] += 1

    ctr = (Counter(c_count))
    mi = ctr.most_common()[0][1]
    ma = ctr.most_common()[-1][1]
    print((mi-ma)//2)

d = dd(int) # {Pair_string: count}
for i in range(1,len(poly)): d[poly[i-1:i+1]] += 1
for step in range(40):
    if step == 10: ans_from(d) # part 1
    nd = d.copy()
    for rule in rules:
        count = d[rule] # do NOT mutate the original dict
        nd[rule] -= count # replace all instances
        nd[rule[0]+rules[rule]] += count # add new instances
        nd[rules[rule]+rule[1]] += count
    d = nd
ans_from(d) # part 2
