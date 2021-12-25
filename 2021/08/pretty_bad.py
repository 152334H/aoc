#!/usr/bin/env python3
from aoc import *
s = sreadlines(div=' | ', name='small')
s = sreadlines(lambda s: s.split(), ' | ')
segment_count = {'a':8, 'b':6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g':7}
segments_to_digit = {2:1, 4:4, 3:7, 7:8}
digit_to_orig = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6: "abdefg", 7: 'acf', 8: "abcdefg", 9: "abcdfg" }
orig_to_digit = {v:k for k, v in digit_to_orig.items()}
segment_count_rev = dd(set)
for k, v in segment_count.items(): segment_count_rev[v].add(k)
part1, part2 = 0,0
for digits,out in s:
    possible = {c: set('abcdefg') for c in 'abcdefg'}
    occur = dd(lambda:0)
    part1 += sum(len(x) in segments_to_digit for x in out)
    for x in digits:
        for c in x: occur[c] += 1
        if len(x) in segments_to_digit:
            for c in x: possible[c] &= set(digit_to_orig[segments_to_digit[len(x)]])
    for c,n in occur.items(): possible[c] &= segment_count_rev[n]
    for c,p in possible.items():
        if len(p) == 1:
            for oth, p2 in possible.items():
                if oth != c: possible[oth] -= p
    possible = {k:v.pop() for k,v in possible.items()}
    part2 += int(''.join('%d'%orig_to_digit[''.join(sorted(possible[c] for c in d))] for d in out))

print(part1)
print(part2)

