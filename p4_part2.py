
grid = []
with open("input_p4.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        row = l.strip()
        row = list(row)
        grid.append(row)


def checkNeighbors(grid, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    num_paper_rolls = 0
    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == '@':
                num_paper_rolls += 1
    if num_paper_rolls < 4:
        return True
    return False

ct = 0
while True:
    curr_ct = 0
    cleared_rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@' and checkNeighbors(grid, i, j):
                cleared_rolls.append((i, j))
                curr_ct += 1

    for (i, j) in cleared_rolls:
        grid[i][j] = 'x'

    ct += curr_ct
    if curr_ct == 0:
        break

print(ct)
