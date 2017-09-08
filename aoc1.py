from sys import exit

solution = 0
step = 0
with open("aoc1.txt") as f:
    for line in f:
        for c in line:
            if c == "(":
                solution += 1
                step += 1
            elif c == ")":
                solution -= 1
                step += 1
                if solution == -1:
                    print step
                    exit()

print solution
