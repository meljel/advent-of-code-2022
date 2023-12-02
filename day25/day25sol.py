import os


toint = { "=" : -2, "-" : -1, "0" : 0, "1" : 1, "2" : 2 }
tosnafu = { 0 : "0", 1 : "1", 2 : "2", 3 : "=", 4 : "-" }

def tr(data):
    lines = data.split("\n")
    return sum([trlit(line) for line in lines])

def trlit(line):
    return sum([toint[c] * 5**i for i, c in enumerate(line[::-1])])

def compound(total):
    s = ""
    while total:
        rem = total % 5
        total //= 5
        if rem > 2: total += 1
        s = tosnafu[rem] + s
    return s

with open(os.path.abspath("day25")+"/input") as file:
    data = file.read().strip()

print(compound(tr(data)))