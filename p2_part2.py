
sum = 0

def isInvalidID(id):
    str_id = str(id)
    for i in range(0, len(str_id) // 2):
        substr = str_id[:i + 1]
        num_repeats = len(str_id) // len(substr)
        if substr * num_repeats == str_id:
            return True
    return False

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
