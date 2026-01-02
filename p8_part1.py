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

for i in range(1000):
    dist, p1, p2 = pairs_with_dist[i]
    root1 = find_root(parents, p1)
    root2 = find_root(parents, p2)
    if root1 != root2:
        parents[root2] = root1
        
components_with_counts = {}
for i in range(len(positions)):
    root = find_root(parents, i)
    if root not in components_with_counts:
        components_with_counts[root] = 0
    components_with_counts[root] += 1

sorted_counts = sorted(components_with_counts.values(), reverse=True)
print(sorted_counts[0] * sorted_counts[1] * sorted_counts[2])
        