
pos = 50
ct = 0

with open("input_p1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())

        num_wraps = abs(value) // 100
        ct += num_wraps
        value = value % 100
        # ct += abs(value) // 100

        if direction == "R":
            new_pos = pos + value
            if new_pos >= 100 and pos > 0:
                ct += 1
        elif direction == "L":
            new_pos = pos - value
            if new_pos <= 0 and pos > 0:
                ct += 1

        pos = new_pos
        pos = pos % 100
        print(line, ct)


print(ct)
