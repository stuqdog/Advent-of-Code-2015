ns = 0
ew = 0
houses = {}
solution = 0
with open("aoc3.txt") as f:
    for line in f:
        for c in line:
            if c == '^':
                ns += 1
            elif c == 'v':
                ns -= 1
            elif c == '<':
                ew -= 1
            elif c == '>':
                ew += 1
            if (ns, ew) not in houses:
                houses[(ns, ew)] = 1
                solution += 1
print(solution)
