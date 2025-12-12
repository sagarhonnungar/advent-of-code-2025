grid = []
with open("input_p4.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        row = l.strip()
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
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@' and checkNeighbors(grid, i, j):
            ct += 1

print(ct)
