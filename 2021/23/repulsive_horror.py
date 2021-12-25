#!/usr/bin/env python3
from aoc import *
s = sreadlines()
E_REQUIRED = {'A':1, 'B': 10, 'C': 100, 'D': 1000}
from dataclasses import dataclass
@dataclass(unsafe_hash=True,order=True)
class Burrow:
    hallway: tuple # a tuple of 7 characters
    rooms: tuple # a room of 4 tuples of constant but unknown length

'''Graph of neighbours, with distance as weights
I don't know how I wrote any of this at all'''
neigh = {}
# distances between hallways
for i in range(1,6): neigh['h',i] = {('h',j):2 for j in (i-1,i+1)}
neigh['h',0] = {('h',1):1}
neigh['h',6] = {('h',5):1}
neigh['h',5]['h',6] = neigh['h',1]['h',0] = 1
# distances between rooms and rooms-hallways
for r in range(4):
    for d in range(4): neigh['r',r,d] = {('r',r,d+dd):1 for dd in (-1,1)}
    del neigh['r',r,0]['r',r,-1]
    del neigh['r',r,3]['r',r,4]
    for h in range(1,3):
        neigh['h',r+h]['r',r,0] = 2
        neigh['r',r,0]['h',r+h] = 2

# APSP
dist = {k:{k:9999999 for k in neigh} for k in neigh}
for k in neigh: dist[k][k] = 0
for k in neigh:
    for k2 in neigh[k]: dist[k][k2] = dist[k2][k] = neigh[k][k2]
for k in dist:
    for i in dist:
        for j in dist: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# set of all places reachable from start
def reachable(burrow,start,end=None) -> Set[Burrow]:
    border = [start]
    seen = set()
    while border:
        i = border.pop()
        if i in seen: continue
        seen.add(i)
        for oth in neigh[i]:
            if oth == end: seen.add(oth)
            if oth[0] == 'r':
                if burrow.rooms[oth[1]][oth[2]] == '.':
                    border.append(oth)
            elif burrow.hallway[oth[1]] == '.':
                border.append(oth)
    return seen
def can_move(burrow,start,end): return end in reachable(burrow,start,end)

def optimise_once(burrow) -> Burrow:
    rooms = list(list(r) for r in burrow.rooms)
    hallway = list(burrow.hallway)

    for hall_i,hall_amp in enumerate(hallway):
        if hall_amp == '.': continue
        desired_room = 'ABCD'.index(hall_amp)
        for depth in reversed(range(len(rooms[0]))):
            # it's assumed here that an amp won't move _within_ a room, but only in/out of a room
            if rooms[desired_room][depth] == '.': # move in
                if can_move(burrow, ('r',desired_room,depth), ('h',hall_i)):
                    rooms[desired_room][depth] = hall_amp
                    hallway[hall_i] = '.'
                    return dist['h',hall_i]['r',desired_room,depth] *E_REQUIRED[hall_amp],\
                        Burrow(tuple(hallway), tuple(tuple(r) for r in rooms))
                break
            elif rooms[desired_room][depth] != hall_amp: # wrong element inside
                break
        # else: raise RuntimeError("wtf")
    return 0, burrow
def optimise(burrow) -> Burrow:
    total_e = 0
    while True:
        e, burrow = optimise_once(burrow)
        if e == 0: return total_e,burrow
        else: total_e += e
def show(burrow): # debug helper
    s = burrow.hallway[0] + ' '.join(burrow.hallway[1:6]) + burrow.hallway[6] + '\n'
    for d in range(len(burrow.rooms[0])):
        s += ' #' + '#'.join(burrow.rooms[r][d] for r in range(4)) + '#\n'
    print(s)
def try_with(start_rooms):
    # run dijkstra. Each "node" is the state of the burrow, each edge involves moving an element out of a room (and potentially into a room)
    q = PQ()
    q.push((0,Burrow(('.',)*7, start_rooms)))
    seen = {}
    while q:
        energy,burrow = q.pop()
        if seen.get(burrow,99999999) <= energy: continue # probably not needed
        seen[burrow] = energy
        # for each room, find the topmost element, and move it somewhere in the hallway
        # add that new burrow to the queue, optimised
        sat_c = 0
        for room in range(4):
            if set(burrow.rooms[room]) == {'ABCD'[room]}:
                sat_c += 1
                continue # this room is satisfied
            # find the topmost element
            for depth in range(len(burrow.rooms[0])):
                if burrow.rooms[room][depth] == '.': continue
                # we've found a top element, now try moving it
                places = reachable(burrow, ('r',room,depth))
                for k in places:
                    if k[0] == 'h':
                        rooms, hallway = list(list(r) for r in burrow.rooms), list(burrow.hallway)
                        hallway[k[1]] = rooms[room][depth]
                        rooms[room][depth] = '.'
                        new_energy = energy + dist[k][('r',room,depth)] * E_REQUIRED[hallway[k[1]]]
                        new_burrow = Burrow(tuple(hallway), tuple(tuple(r) for r in rooms))
                        new_new_e, new_new_burrow = optimise(new_burrow)
                        q.push((new_energy + new_new_e,new_new_burrow))
        if sat_c == 4: return energy

p1_rooms = tuple(tuple(s[2+d][3+r*2] for d in range(2)) for r in range(4))
p2 = try_with(tuple(tuple(p1_rooms[r][0] + ["DD","CB","BA","AC"][r] + p1_rooms[r][1]) for r in range(4)))
for r in range(4): del neigh['r',r,1]['r',r,2]
print(try_with(p1_rooms))
print(p2)
