
from collections import defaultdict
import math

red_tiles = []
max_x = 0
max_y = 0
row_tiles = defaultdict(list)
col_tiles = defaultdict(list)
with open("input_p9.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        pos = [int(v) for v in l.strip().split(",")]
        red_tiles.append(pos)
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])
        row_tiles[pos[1]].append(pos[0])
        col_tiles[pos[0]].append(pos[1])

row_mins = defaultdict(lambda: float('inf'))
row_maxs = defaultdict(lambda: float('-inf'))
col_mins = defaultdict(lambda: float('inf'))
col_maxs = defaultdict(lambda: float('-inf'))

for j in range(len(red_tiles)):
    curr_x, curr_y = red_tiles[j]
    if j == 0:
        prev_x, prev_y = red_tiles[-1]
    else:   
        prev_x, prev_y = red_tiles[j-1]
    if curr_x == prev_x:
        for y in range(min(curr_y, prev_y), max(curr_y, prev_y)+1):
            col_mins[curr_x] = min(col_mins[curr_x], y)
            col_maxs[curr_x] = max(col_maxs[curr_x], y)
            row_mins[y] = min(row_mins[y], curr_x)
            row_maxs[y] = max(row_maxs[y], curr_x)
    elif curr_y == prev_y:
        for x in range(min(curr_x, prev_x), max(curr_x, prev_x)+1):
            col_mins[x] = min(col_mins[x], curr_y)
            col_maxs[x] = max(col_maxs[x], curr_y)
            row_mins[curr_y] = min(row_mins[curr_y], x)
            row_maxs[curr_y] = max(row_maxs[curr_y], x)

max_rect_area = 0
for (x1, y1) in red_tiles:
    curr_min_x = row_mins[y1]
    curr_max_x = row_maxs[y1]
    for y in range(y1, max_y+1):
        if y in row_tiles:
            for x in row_tiles[y]:
                if x >= curr_min_x and x <= curr_max_x and x1 >= curr_min_x and x1 <= curr_max_x:
                    area = (abs(y - y1) + 1) * (abs(x - x1) + 1)
                    if area > max_rect_area:
                        max_rect_area = area
                        print("New max area:", max_rect_area, "at", (x1, y1), (x, y))
        curr_min_x = max(curr_min_x, row_mins[y])
        curr_max_x = min(curr_max_x, row_maxs[y])



print(max_rect_area)
