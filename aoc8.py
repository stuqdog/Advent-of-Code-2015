from sys import exit

string_total = 0
string_diff = 0

# def create_short_string(line):
#     hex_mode = False
#     short_string = ''
#     for c in line:
#         if not hex_mode and c not in ['"', "''"]

with open("aoc8.txt") as f:
    for line in f:
        string_total += sum(1 for c in line.strip())
        for i, c in enumerate(line.strip('\n\"')):
            # if c in ["'", '"']:
            #     string_diff += 1
            if c == "\\" and line[i + 1] not in ["'", '"']:
                string_diff += 3

print(string_diff)
