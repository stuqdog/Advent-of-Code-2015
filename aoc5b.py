def check_if_nice(line):
    if all(line[x-2:x] not in line[x:] for x in range(2, len(line) - 1)):
        return 0
    if any(line[x] == line[x-2] for x in range(2, len(line))):
        return 1
    return 0

with open("aoc5.txt") as f:
    print((sum(check_if_nice(line) for line in f)))
