import heapq


def getcals(data):
    lines = data.split("\n\n")
    return [perelf(line.split("\n")) for line in lines]

def perelf(cals):
    return sum([int(cal) for cal in cals])

def topthree(nums):
    return sum(heapq.nlargest(3, nums))

with open("./day01/input.txt") as file:
    data = file.read().strip()

nums = getcals(data)
print(max(nums))
print(topthree(nums))