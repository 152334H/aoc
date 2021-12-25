#!/usr/bin/env python3
from aoc import *
numbers, *boards = sreadlinelines(div='\n')
numbers = Map(int,numbers[0].split(','))
boards = [[[int(s) for s in line.split() if s] for line in board] for board in boards]

def is_bingo(board, nums):
    crosses = [[True if board[i][j] in nums else False for j in range(5)] for i in range(5)]
    for i in range(5):
        if all(crosses[i][j] for j in range(5)) or\
           all(crosses[j][i] for j in range(5)): return True
    return False

def solve(board: List[List[int]], nums: Set[int], last: int):
    print(sum(set(sum(board,[])) - nums) * last)

last = None
nums, seen = set(), set()
for n in numbers:
    nums.add(n)
    for i in range(len(boards)):
        if i in seen: continue
        board = boards[i]
        if is_bingo(board, nums):
            last = (board, nums.copy(), n)
            if not seen: solve(*last) # part 1 is here
            seen.add(i)
solve(*last)
