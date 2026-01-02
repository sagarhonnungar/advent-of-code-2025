# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
from collections import defaultdict
outputs = defaultdict(list)
start = "you"
with open("input_p11.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        parts = l.strip().split(": ")
        key = parts[0]
        values = parts[1].split()
        for v in values:
            outputs[key].append(v)

num_paths = 0
memo = {}
def count_paths(node):
    if node == "out":
        return 1
    if node in memo:
        return memo[node]
    total = 0
    for neighbor in outputs[node]:
        total += count_paths(neighbor)
    memo[node] = total
    return total

num_paths = count_paths(start)
print(num_paths)


