def check_if_nice(line):
    if sum(1 for c in line if c in 'aeiou') < 3:
        return 0
    if all(line[x] != line[x - 1] for x in range(1, len(line))):
        return 0
    if any(x in line for x in ['ab', 'cd', 'pq', 'xy']):
        return 0
    return 1

with open("aoc5.txt") as f:
    print((sum(check_if_nice(line) for line in f)))
