#!/usr/bin/env python3
from aoc import *
s = sreadlines()
players = [(int(l[-1]),0) for l in s]
dp = [dd(int,{players[0]: 1}), dd(int,{players[1]:1})] # this is for part 2

# diceroll generator
rolls = 0
def dice():
    while 1:
        for i in range(100): yield i+1
roll = dice()
# part 1
while 1:
    for p in range(2):
        pos,score = players[p]
        add = sum(next(roll) for _ in range(3))
        rolls += 3
        pos += add-1
        pos %= 10
        pos += 1
        players[p] = (pos,score+pos)
        if score+pos >= 1000: break
    else: continue
    break
print(rolls*min(p[1] for p in players))

# generate frequency lookup for 3 rolls of the quantum dice
pspace = {}
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4): pspace[a+b+c] = 1+pspace.get(a+b+c,0)
# solve for part 2
universes = [1,1]
winners = [0,0]
while any(dp):
    for p in range(2):
        new_d = dd(int)
        for (pos,score),cnt in dp[p].items():
            for add,add_cnt in pspace.items():
                np = pos-1+add
                np %= 10
                np += 1
                if score+np >= 21: winners[p] += cnt*add_cnt*universes[not p]
                else: new_d[(np,score+np)] += cnt*add_cnt
        dp[p] = new_d
        universes[p] = sum(dp[p].values())
print(max(winners))
