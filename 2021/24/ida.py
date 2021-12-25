from z3 import *
def int64(v): return v&0xffffffffffffffff
def add_constraints(s,inp):
    for d in inp:
        s.add(d> 0)
        s.add(d< 10)

    v42 = (inp[0] + 7) * (inp[0] != 12) % 26 + 13 != inp[1];
    v43 = (inp[1] + 8) * v42 + (inp[0] + 7) * (inp[0] != 12) * (25 * v42 + 1);
    v44 = v43 % 26 + 13 != inp[2];
    v45 = (inp[2] + 10) * v44 + v43 * (25 * v44 + 1);
    v46 = v45 / 26;
    v47 = v45 % 26 - 2 != inp[3];
    v48 = ((inp[3] + 4) * v47 + (25 * v47 + 1) * (v45 / 26)) / 26;
    v49 = (inp[3] + 4) * v47 + (25 * v47 + 1) * v46 - 26 * v48;
    v50 = (inp[4] + 4) * (v49 - 10 != inp[4]) + v48 * (25 * (v49 - 10 != inp[4]) + 1);
    v51 = v50 % 26 + 13 != inp[5];
    v52 = (inp[5] + 6) * v51 + v50 * (25 * v51 + 1);
    v53 = v52 / 26;
    v54 = v52 % 26 - 14 != inp[6];
    v55 = ((inp[6] + 11) * v54 + (25 * v54 + 1) * (v52 / 26)) / 26;
    v56 = (inp[6] + 11) * v54 + (25 * v54 + 1) * v53 - 26 * v55;
    v57 = (inp[7] + 13) * (v56 - 5 != inp[7]) + (25 * (v56 - 5 != inp[7]) + 1) * v55;
    v58 = v57 % 26 + 15 != inp[8];
    v59 = (inp[8] + 1) * v58 + (25 * v58 + 1) * v57;
    v60 = v59 % 26 + 15 != inp[9];
    v61 = (inp[9] + 8) * v60 + (25 * v60 + 1) * v59;
    v62 = v61 % 26 - 14 != inp[10];
    v63 = (inp[10] + 4) * v62 + v61 / 26 * (25 * v62 + 1);
    v64 = v63 % 26 + 10 != inp[11];
    v65 = ((inp[11] + 13) * v64 + (25 * v64 + 1) * v63) / 26;
    v66 = ((inp[11] + 13) * v64 + (25 * v64 + 1) * v63) % 26 - 14 != inp[12];
    v67 = (inp[12] + 4) * v66 + (25 * v66 + 1) * v65;
    v68 = v67 % 26 - 5 != inp[13];
    res = (25 * v68 + 1) * (v67 / 26) + (inp[13] + 14) * v68;

    tot = 0
    for d in inp: tot = tot*10+d
    s.add(res==0)
    return tot

def solve(inp, part1=True):
    s = Optimize()
    value = add_constraints(s,inp)
    if part1: s.maximize(value)
    else: s.minimize(value)
    assert s.check() == sat
    m = s.model()
    return m.eval(value)

inp = [z3.Int('x%d'%i) for i in range(14)]

print("Part 1:", solve(inp, True))
print("Part 2:", solve(inp, False))
