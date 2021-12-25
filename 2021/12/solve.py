#!/usr/bin/env python3
from aoc import *
s = sreadlines(div='-')

g = defaultdict(set)
for u,v in s:
    g[u].add(v)
    g[v].add(u)

def dfs(n, vis, pred) -> int:
    if n.islower() and pred(vis,n): return 0
    if n == 'end': return 1
    vis[n] += 1
    if n.islower() and vis[n] > 1: vis['doubleadded'] = True
    res = sum(dfs(nxt, vis, pred) for nxt in g[n])
    if n.islower() and vis[n] > 1: vis['doubleadded'] = False
    vis[n] -= 1
    return res

def solve(p): return dfs('start', dd(int), p)
print(solve(lambda vis,n: vis[n]))
print(solve(lambda vis,n: (vis[n] > 1 or \
        (vis[n] and (vis['doubleadded'] or n == 'start')))))
