f = ["ABC", "XYZ"]

def totalscore(lines, relative):
    return sum([score(*line.split(), relative) for line in lines])

def score(one, two, relative):
    f1, f2 = f[0].index(one), f[1].index(two)
    if relative: # Problem 2
        wins, f2 = f2, (f2 + f1 - 1) % 3
    else: wins = (f2 - f1 + 1) % 3 # Problem 1
    return f2 + 1 + 3 * wins

with open("./day02/input.txt") as file:
    lines = file.readlines()

print(totalscore(lines, False))
print(totalscore(lines, True))
