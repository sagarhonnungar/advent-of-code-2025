
import bisect

with open("input_p5.txt", "r") as f:
    lines = f.readlines()
    fresh_ranges = []
    avail_ids = []
    for line in lines:
        r = line.strip().split("-")
        if len(r) == 2:
            fresh_ranges.append((int(r[0]), int(r[1])))
        elif r[0] == "":
            continue
        else:
            avail_ids.append(int(r[0]))

sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
merged_ranges = []
for current in sorted_ranges:
    if not merged_ranges:
        merged_ranges.append(current)
    else:
        last = merged_ranges[-1]
        if current[0] <= last[1] + 1:
            merged_ranges[-1] = (last[0], max(last[1], current[1]))
        else:
            merged_ranges.append(current)

tot_fresh = 0
for r in merged_ranges:
    tot_fresh += (r[1] - r[0] + 1)

print(tot_fresh)

