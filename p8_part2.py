import math

positions = []
with open("input_p8.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        pos = [int(v) for v in l.strip().split(",")]
        positions.append(pos)


def get_straight_line_distance(p1, p2) -> int:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

pairs_with_dist = []
for i in range(len(positions)-1):
    for j in range(i+1, len(positions)):
        dist = get_straight_line_distance(positions[i], positions[j])
        pairs_with_dist.append((dist, i, j))

pairs_with_dist.sort()

parents = {i: i for i in range(len(positions))}

def find_root(parents, node):
    while parents[node] != node:
        node = parents[node]
    return node

component_counts = {i: 1 for i in range(len(positions))}
for i in range(len(pairs_with_dist)):
    dist, p1, p2 = pairs_with_dist[i]
    root1 = find_root(parents, p1)
    root2 = find_root(parents, p2)
    if root1 != root2:
        parents[root2] = root1
        component_counts[root1] += component_counts[root2]
        component_counts[root2] = 0
        if component_counts[root1] == len(positions):
            pos1 = positions[p1]
            pos2 = positions[p2]
            print(pos1[0]*pos2[0])
            break
