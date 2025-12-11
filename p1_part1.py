
pos = 50
ct = 0
with open("input_p1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())
        if direction == "R":
            pos += value
        elif direction == "L":
            pos -= value

        pos = pos % 100
        if pos == 0:
            ct += 1


print(ct)
