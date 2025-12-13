
timelines_ct = 0
cache = {}

def get_timelines_ct(lines, i, j) -> int:
    if (i, j) in cache:
        return cache[(i, j)]
    if i == len(lines) - 1:
        if j >= 0 and j < len(lines[0]):
            return 1
        else:
            return 0
    if lines[i+1][j] == '^':
        res = get_timelines_ct(lines, i+1, j+1) + get_timelines_ct(lines, i+1, j-1)
    else:
        res = get_timelines_ct(lines, i+1, j)
    cache[(i, j)] = res
    return res

with open("input_p7.txt", "r") as f:
    lines = f.readlines()
    lines = [list(l.strip()) for l in lines]

    for j in range(len(lines[0])):
        if lines[0][j] == 'S':
            timelines_ct = get_timelines_ct(lines, 1, j)

print(timelines_ct)
