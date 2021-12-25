#!/usr/bin/env python3
from aoc import *
class List(list):
    def __init__(self,ls):
        self.par = (None,None)
        super().__init__(ls)
def listenum(ls): return ((i,l) for i,l in enumerate(ls) if isinstance(l,list))
def trav(ls,par=None):
    for i,l in listenum(ls):
        ls[i] = List(l)
        l = ls[i]
        l.par = (ls,i)
        trav(l,ls)
s = [List(l) for l in sreadlines(eval)]
for l in s: trav(l)

def find(f,ls,i): # find the left or right element
    f1,sign,f2 = f
    if i in f1(ls):
        i += sign
        while isinstance(ls[i],list): i = f2(ls:=ls[i])
        return ls,i
    return (None,None) if ls.par[0] is None else find(f,*ls.par)
left  = (lambda ls: range(1,999999), -1, lambda ls: len(ls)-1)
right = (lambda ls: range(len(ls)-1), 1, lambda ls: 0)

def explode_if_needed(ls,depth=0):
    if depth < 3: return bool(sum(explode_if_needed(l,depth+1) for i,l in listenum(ls)))
    else: # note: this assumes that max depth is 4.
        worked = False
        for i,(a,b) in listenum(ls):
            worked = True
            ls[i] = 0
            for f,v in zip((right,left),(b,a)):
                ref,ind = find(f,ls,i)
                if ref is not None: ref[ind] += v
        return worked

def split_if_needed(ls):
    for i in range(len(ls)):
        if isinstance(ls[i],list):
            if split_if_needed(ls[i]): return True
        elif ls[i] >= 10:
            ls[i] = List([ls[i]//2, (ls[i]+1)//2])
            ls[i].par = (ls,i)
            return True
    return False

def add_snails(a,b):
    ls = List([a,b])
    a.par,b.par = (ls,0),(ls,1)
    while explode_if_needed(ls) or split_if_needed(ls): pass
    return ls
def mag(pair):
    left = pair[0] if isinstance(pair[0],int) else mag(pair[0])
    right = pair[1] if isinstance(pair[1],int) else mag(pair[1])
    return left*3+right*2

from copy import deepcopy
print(mag(reduce(add_snails,deepcopy(s))))

print("part 2 will take a while")
ma = -9999999999999
for i,j in permutations(range(len(s)),2):
    a,b = deepcopy(s[i]),deepcopy(s[j])
    ma = max(ma, mag(add_snails(a,b)))
print(ma)
