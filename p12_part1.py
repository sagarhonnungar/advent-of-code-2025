from collections import defaultdict

presents = {}
tree_regions = []

with open("input_p12.txt", "r") as file:
    lines = file.readlines()

    curr_present_id = None
    for line in lines:
        line = line.strip()
        if line:
            if line[-1] == ":":
                curr_present_id = int(line[:-1])
                presents[curr_present_id] = []
            elif line[0] == "#" or line[0] == ".":
                presents[curr_present_id].append(line)
            else:
                shape, present_counts = line.split(":")
                shape = shape.strip()
                present_counts = [int(count) for count in present_counts.split()]
                tree_regions.append({
                    "width": int(shape.split("x")[0]),
                    "length": int(shape.split("x")[1]),
                    "present_counts": present_counts
                })


max_present_width = max([len(present[0]) for present in presents.values()])
max_present_length = max([len(present) for present in presents.values()])

print(max_present_width, max_present_length)

present_areas = defaultdict(int)
for pnum, present in presents.items():
    for row in present:
        for cell in row:
            if cell == "#":
                present_areas[pnum] += 1

ct = 0
for region in tree_regions:
    if region["width"] < max_present_width or region["length"] < max_present_length:
        continue

    req_area = 0
    for pnum, count in enumerate(region["present_counts"]):
        req_area += count * present_areas[pnum]
    if req_area > region["width"] * region["length"]:
        continue    
    else:
        ct += 1

print(ct)
