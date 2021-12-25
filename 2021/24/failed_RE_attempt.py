#!/usr/bin/env python3
from aoc import *
from z3 import *
s = sreadlines(div=' ')
model_num = '[1-9]{14}'

def attempt(it,stop_at=99):
    vals = {c:0 for c in 'wxyz'}
    def get_right(s):
        if s.isdigit() or ( len(s) > 1 and s[0] == '-' and s[1:].isdigit() ):
            return int(s)
        else:
            return vals[s]
    for op,*args in s:
        if op == 'inp':
            if not stop_at: return vals
            stop_at -= 1
            vals[args[0]] = int(next(it))
        elif op == 'add':
            vals[args[0]] += get_right(args[1])
        elif op == 'mul':
            vals[args[0]] *= get_right(args[1])
        elif op == 'div':
            vals[args[0]] //= get_right(args[1])
            if vals[args[0]]<0: raise RuntimeError
        elif op == 'mod':
            vals[args[0]] %= get_right(args[1])
        elif op == 'eql':
            vals[args[0]] = bool(vals[args[0]] == get_right(args[1]))
    return vals['z']

'''
for i in reversed(range(10**14)):
    it = iter(str(i))
    if attempt(it) == 0: print(i)
'''
it = iter('13191913782653')
print(attempt(it))
'''
for i in range(1,10):
    it = iter(str(i)*14)
    print(attempt(it))
'''
def f1(v): return {'w':v, 'x': True, 'y': 7+v, 'z': 7+v}
def f2(d,v): return {'w':v, 'x': True, 'y': 8+v, 'z': d['y']*26+8+v}
def f3(d,v): return {'w':v, 'x': True, 'y': 10+v, 'z': d['z']*26+10+v}
for i in range(1,10): assert f1(i) == attempt(iter(str(i)*14),1)
for i in range(1,10): assert f2(f1(1),i) == attempt(iter('1'+str(i)),2)
for i in range(1,10): assert f3(f2(f1(8),8),i) == \
        attempt(iter('88'+str(i)),3)
for i in range(10):
    it = iter('11'+str(i)+'1'*11)
    print(attempt(it,3))
    print(f3(f2(f1(1),1),i))
    print('---')
    it = iter('12'+str(i)+'1'*11)
    print(attempt(it,3))
    print(f3(f2(f1(1),2),i))
    print('---')



