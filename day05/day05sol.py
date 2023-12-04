import re


def craterepr(state: str):
    crates = ["" for i in range(1, 10)]
    for line in state.split("\n")[len(crates)-2::-1]:
        for i, v in enumerate(re.findall(r"\s{4}|[A-Z]", line)):
            if " " not in v: crates[i] += v
    return crates

def transform(lines, crates: dict, transfer):
    for line in lines.split("\n"):
        n, a, b = map(int, map(line.split().__getitem__, [1,3,5]))
        crates[a-1], moving = crates[a-1][:-n], crates[a-1][-n:]
        if transfer: crates[b-1] += moving
        else: crates[b-1] += moving[::-1]
    return "".join(z[-1] for z in crates)

with open("./day05/input.txt") as file:
    state, lines = file.read().strip().split("\n\n")

print(transform(lines, craterepr(state), False))
print(transform(lines, craterepr(state), True))
