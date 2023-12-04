
def total(lines, overlapOnly):
    return sum([contains(line, overlapOnly) for line in lines])

def contains(line, overlapOnly):
    l1, r1 = map(int, line.split(",")[0].split("-"))
    l2, r2 = map(int, line.split(",")[1].split("-"))
    if overlapOnly: return (l1<=l2 and l2<=r1) or (l2<=l1 and l1<=r2)
    return (l1<=l2 and r1>=r2) or (l1>=l2 and r1<=r2)

with open("./day04/input.txt") as file:
    lines = file.read().strip().split("\n")

print(total(lines, False))
print(total(lines, True))
