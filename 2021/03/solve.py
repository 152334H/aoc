#!/usr/bin/env python3
from aoc import *
s = sreadlines()
# useful funcs for in both parts
def two_most(gen): return Counter(gen).most_common(2)
def resolve(ls): return int(''.join(ls),2)
def mul(f): return f(1)*f(0)

# part 1
res = [tuple(t[0] for t in two_most(l[i] for l in s)) for i in range(len(s[0]))] # use list because res is used twice
print(mul(lambda i: resolve(t[i] for t in res)))

# part 2
def part2(typ: bool): # typ: True == CO2, False == O2
    numbers = set(s) # assert len(set(s)) == len(s)
    for i in range(len(s[0])):
        if len(numbers) == 1: break
        ctr = two_most(l[i] for l in numbers)
        keep = ctr[typ][0] if ctr[0][1] != ctr[1][1] else '10'[typ]
        for l in list(numbers):
            if l[i] != keep: numbers.remove(l)
    else:
        if len(numbers) != 1: raise RuntimeError
    return resolve(numbers.pop())
print(mul(part2))
