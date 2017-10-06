with open("aoc2.txt") as f:
    gifts = [line.strip().split('x') for line in f]
new_gifts = []
for gift in gifts:
    new_gifts.append(sorted([int(gift[0]), int(gift[1]), int(gift[2])]))

solution = 0
for gift in new_gifts:
    solution += (gift[0] * 3 * gift[1] + gift[1] * 2 * gift[2]
                 + gift[2] * gift[0] * 2)
print(solution)
