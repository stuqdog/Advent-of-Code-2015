import re

grid = []

for x in range(1000):
    grid.append([])
    for y in range(1000):
        grid[x].append(0)

with open("aoc6.txt") as f:
    for line in f:
        check = re.match("turn on (\d+),(\d+) through (\d+),(\d+)", line)
        if check:
            for x in range(int(check.group(1)), int(check.group(3)) + 1):
                for y in range(int(check.group(2)), int(check.group(4)) + 1):
                    grid[x][y] = 1
        check = re.match("toggle (\d+),(\d+) through (\d+),(\d+)", line)
        if check:
            for x in range(int(check.group(1)), int(check.group(3)) + 1):
                for y in range(int(check.group(2)), int(check.group(4)) + 1):
                    grid[x][y] = abs(grid[x][y] - 1)
        check = re.match("turn off (\d+),(\d+) through (\d+),(\d+)", line)
        if check:
            for x in range(int(check.group(1)), int(check.group(3)) + 1):
                for y in range(int(check.group(2)), int(check.group(4)) + 1):
                    grid[x][y] = 0

def grid_math():
    for column in grid:
        for light in column:
            yield light

print(sum(grid_math()))
