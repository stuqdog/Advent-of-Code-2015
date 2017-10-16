import re

wires = {}
rules = []
break_time = False

def determine_rule(line):
    rule = re.match("(.+) AND (.+) \-> (.+)", line)
    if rule:
        return "and", rule
    rule = re.match("(.+) OR (.+) \-> (.+)", line)
    if rule:
        return "or", rule
    rule = re.match("(.+) LSHIFT (\d+) \-> (.+)", line)
    if rule:
        return "lshift", rule
    rule = re.match("(.+) RSHIFT (\d+) \-> (.+)", line)
    if rule:
        return "rshift", rule
    rule = re.match("NOT (.+) \-> (.+)", line)
    if rule:
        return "not", rule
    rule = re.match("(\d+) \-> (.+)", line)
    if rule:
        return "assign_num", rule
    rule = re.match("(.+) \-> (.+)", line)
    if rule:
        return "assign_wire", rule
    return "error", line

with open("aoc7.txt") as f:
    for line in f:
        rule_type, rule = determine_rule(line)
        print(rule_type)
        rules.append((rule_type, rule))

while True:
    to_delete = []
    for i, line in enumerate(rules):
        if line[0] == "assign_num":
            value = bin(int(line[1].group(1)))[2:]
            value = '0' * (16 - len(value)) + value
            wires[line[1].group(2)] = value
            to_delete.append(i)
        elif line[0] == "assign_wire":
            if line[1].group(1) in wires:
                wires[line[1].group(2)] = wires[line[1].group(1)]
                to_delete.append(i)
            else:
                pass
        elif line[0] == 'and':
            if line[1].group(1) == '1' and line[1].group(2) in wires:
                value = '0' * 15 + wires[line[1].group(2)][15]
                wires[line[1].group(3)] = value
                to_delete.append(i)
            elif line[1].group(1) in wires and line[1].group(2) in wires:
                value = ''
                for x in range(16):
                    if (wires[line[1].group(1)][x] == '1'
                          and wires[line[1].group(2)][x] == '1'):
                        value += '1'
                    else:
                        value += '0'
                wires[line[1].group(3)] = value
                to_delete.append(i)
        elif line[0] == 'or':
            if line[1].group(1) in wires and line[1].group(2) in wires:
                value = ''
                for x in range(16):
                    if (wires[line[1].group(1)][x] == '0'
                          and wires[line[1].group(2)][x] == '0'):
                        value += '0'
                    else:
                        value += '1'
                wires[line[1].group(3)] = value
                to_delete.append(i)

        elif line[0] == 'lshift':
            if line[1].group(1) in wires:
                wires[line[1].group(3)] = (
                            wires[line[1].group(1)][int(line[1].group(2)):]
                            + ('0' * int(line[1].group(2))))
                to_delete.append(i)
        elif line[0] == 'rshift':
            if line[1].group(1) in wires:
                wires[line[1].group(3)] = (('0' * int(line[1].group(2))) +
                            wires[line[1].group(1)][:16 - int(line[1].group(2))])
                            # + wires[line[1].group(1)][:16 - int(line[1].group(2))])
                to_delete.append(i)
        elif line[0] == 'not':
            if line[1].group(1) in wires:
                value = ''
                for x in range(16):
                    if wires[line[1].group(1)][x] == '1':
                        value += '0'
                    else:
                        value += '1'
                wires[line[1].group(2)] = value
                to_delete.append(i)
        else:
            print("Something has gone wrong with line: {}".format(rule))
            break
    if len(to_delete) == 0 and len(rules) != 0:
        print("Something is wrong")
        for rule in rules:
            print(rule[1].group(0))
        print(wires)
        break
    if not rules:
        break
    for index in reversed(to_delete):
        del rules[index]


if 'a' in wires:
    print(wires['a'])
