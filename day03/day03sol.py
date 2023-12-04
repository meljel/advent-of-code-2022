import re


def totalvalue(lines, group3):
    if not group3:
        return sum([value(line) for line in lines])
    else: return sum([badgeval(*lines[3*i:3*i+3]) for i in range(len(lines)//3)])

def value(line):
    one, two = line[:len(line)//2], line[len(line)//2:]
    return priority(re.findall("["+one+"]", two)[0])

def priority(c): return ord(c)-96 if ord(c)>96 else ord(c)-38

def badgeval(l1, l2, l3):
    ins = set(l1).intersection(set(l2).intersection(set(l3.replace("\n",""))))
    return priority(ins.pop())

with open("./day03/input.txt") as file:
    lines = file.readlines()

print(totalvalue(lines, False))
print(totalvalue(lines, True))