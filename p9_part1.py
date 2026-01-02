
red_tiles = []
with open("input_p9.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        pos = [int(v) for v in l.strip().split(",")]
        red_tiles.append(pos)

top_points = {}
bottom_points = {}
left_points = {}
right_points = {}
for t in red_tiles:
    x, y = t
    if x not in top_points or y < top_points[x][1]:
        top_points[x] = t
    if x not in bottom_points or y > bottom_points[x][1]:
        bottom_points[x] = t
    if y not in left_points or x < left_points[y][0]:
        left_points[y] = t
    if y not in right_points or x > right_points[y][0]:
        right_points[y] = t

max_rect_area = 0
for x1 in top_points:
    for x2 in bottom_points:
        area = (bottom_points[x2][1] - top_points[x1][1] + 1) * (x2 - x1 + 1)
        if area > max_rect_area:
            max_rect_area = area

for y1 in left_points:
    for y2 in right_points:
        area = (right_points[y2][0] - left_points[y1][0] + 1) * (y2 - y1 + 1)
        if area > max_rect_area:
            max_rect_area = area

print(max_rect_area)
