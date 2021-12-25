#!/usr/bin/env python3
from aoc import *
from z3 import *
s = sreadlines(div=' ')
model_num = '[1-9]{14}'

def attempt(it):
    vals = {c:0 for c in 'wxyz'}
    def get_right(s):
        if s.isdigit() or ( len(s) > 1 and s[0] == '-' and s[1:].isdigit() ):
            return int(s)
        else:
            return vals[s]
    for op,*args in s:
        if op == 'inp':
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

vals = dd(int)
code = [Int('c%d'%i) for i in range(14)]
S = Solver()
for i in range(14):
    S.add(code[i] > 0)
    S.add(code[i] <= 9)

def get_right(s):
    if s.isdigit() or ( len(s) > 1 and s[0] == '-' and s[1:].isdigit() ):
        return int(s)
    else: return vals[s]

ind = 0
for op,*args in s:
    if op == 'inp':
        vals[args[0]] = code[ind]
        ind += 1
    elif op == 'add':
        vals[args[0]] += get_right(args[1])
    elif op == 'mul':
        vals[args[0]] *= get_right(args[1])
    elif op == 'div':
        #mod = vals[args[0]] % get_right(args[1])
        #vals[args[0]] = (vals[args[0]]-mod) / get_right(args[1])
        #vals[args[0]] //= get_right(args[1])
        vals[args[0]] /= get_right(args[1])
        #if vals[args[0]]<0: raise RuntimeError
    elif op == 'mod':
        vals[args[0]] %= get_right(args[1])
    elif op == 'eql':
        vals[args[0]] = If(vals[args[0]] == get_right(args[1]), 1, 0)
    #print(vals)


S.add(vals['z'] == 0)
#S.check()
for c in code:
    ma = 9
    while 1:
        S.push()
        S.add(c >= ma)
        if S.check() == sat: break
        S.pop()
        print(ma, 'failed for ', c)
        ma -= 1
    m = S.model()
    print(int(''.join(str(m[c]) for c in code)))
print(S.model())
'''
S.check()
for c in code:
    while 1:
        m = S.model()
        print(int(''.join(str(m[c]) for c in code)))
        if m[c] == 9:
            S.add(c == m[c])
            break
        S.push() # backtracking
        S.add(c > m[c])
        if S.check() == unsat:
            S.pop()
            S.add(c == m[c])
            break
    print(code)
print(S.model())
'''
