
sum = 0

def isInvalidID(id):
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return False
    mid = len(str_id) // 2
    first_half = str_id[:mid]
    second_half = str_id[mid:]
    return first_half == second_half

with open("input_p2.txt", "r") as file:
    ranges = file.readline()
    ranges = ranges.strip().split(",")

    for r in ranges:
        bounds = r.split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])
        for i in range(lower, upper + 1):
            if isInvalidID(i):
                sum += i

print(sum)
