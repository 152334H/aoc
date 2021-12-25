#!/usr/bin/env python3
from aoc import *
s = sread()
binary = bin(int.from_bytes(bytes.fromhex(s),'big'))[2:].rjust(len(s)*4,'0')
part1 = 0
def parse_packets(b_str: str, max_packets: int=99999999999):
    global part1
    packets = []
    i = 0
    while i+6 < len(b_str) and len(packets) < max_packets:
        ver = int(b_str[i:i+3],2)
        part1 += ver
        typ_id = int(b_str[i+3:i+6],2)
        i += 6
        if typ_id == 4:
            n = ''
            while b_str[i] == '1':
                n += b_str[i+1:i+5]
                i += 5
            n += b_str[i+1:i+5]
            i += 5
            packets.append(int(n,2))
        else: # operator
            len_id = int(b_str[i],2)
            i += 1
            if len_id == 0: # next 15 bits
                total_len_of_subpackets = int(b_str[i:i+15],2)
                i += 15
                added,added_len = parse_packets(b_str[i:i+total_len_of_subpackets])
            elif len_id == 1: # next 11 bits
                number_of_subpackets = int(b_str[i:i+11],2)
                i += 11
                added,added_len = parse_packets(b_str[i:], number_of_subpackets)
            i += added_len
            if typ_id == 0:
                packets.append(sum(added))
            elif typ_id == 1:
                packets.append(prod(added))
            elif typ_id == 2:
                packets.append(min(added))
            elif typ_id == 3:
                packets.append(max(added))
            elif typ_id == 5:
                assert len(added) == 2
                packets.append(int(bool(added[0] > added[1])))
            elif typ_id == 6:
                assert len(added) == 2
                packets.append(int(bool(added[0] < added[1])))
            elif typ_id == 7:
                assert len(added) == 2
                packets.append(int(bool(added[0] == added[1])))
    return packets,i
print('part2:', parse_packets(binary)[0][0])
print(part1)
