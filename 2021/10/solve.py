#!/usr/bin/env python3
from aoc import *

matching = {'{': '}', '[': ']', '(': ')', '<': '>'}
matching_reverse = {v: k for k, v in matching.items()}
def analyse(l: str) -> Union[str, List[str]]:
    stack = []
    for c in l:
        if c in matching: stack.append(c)
        elif c in matching_reverse:
            if not stack: raise RuntimeError
            if matching_reverse[c] != stack.pop():
                return c # return first corrupt character
        else: raise RuntimeError
    return [matching[c] for c in reversed(stack)] # characters to add

part1 = 0
value = {')': 3, ']': 57, '}': 1197, '>': 25137}
part2 = []
value2 = {')': 1, ']': 2, '}': 3, '>': 4}
for outcome in sreadlines(analyse):
    if isinstance(outcome,str): part1 += value[outcome]
    else: part2.append(reduce(lambda x,y: x*5+y,
            (value2[c] for c in outcome)))

print(part1)
part2.sort()
print(part2[len(part2)//2])

