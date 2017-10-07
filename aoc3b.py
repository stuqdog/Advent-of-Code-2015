ns = 0
ns_r = 0
ew = 0
ew_r = 0
houses = {}
solution = 0
s_or_r = 0
with open("aoc3.txt") as f:
    for line in f:
        for c in line:
            if c == '^':
                if s_or_r % 2 == 0:
                    ns += 1
                else:
                    ns_r += 1
            elif c == 'v':
                if s_or_r % 2 == 0:
                    ns -= 1
                else:
                    ns_r -= 1
            elif c == '<':
                if s_or_r % 2 == 0:
                    ew -= 1
                else:
                    ew_r -= 1
            elif c == '>':
                if s_or_r % 2 == 0:
                    ew += 1
                else:
                    ew_r += 1
            if s_or_r % 2 == 0 and (ns, ew) not in houses:
                houses[(ns, ew)] = 1
                solution += 1
            elif s_or_r % 2 == 1 and (ns_r, ew_r) not in houses:
                houses[(ns_r, ew_r)] = 1
                solution += 1
            s_or_r += 1
print(solution)
