
tot = 0
with open("input_p3.txt", "r") as f:
    banks = f.readlines()
    for b in banks:
        b = b.strip()
        max_val = b[0]
        max_idx = 0
        for i in range(1, len(b)-1):
            if b[i] > max_val:
                max_val = b[i]
                max_idx = i

        max_val_2 = b[max_idx+1]
        for i in range(max_idx+1, len(b)):
            if b[i] > max_val_2:
                max_val_2 = b[i]

        tot += int(max_val)*10 + int(max_val_2)

print(tot)
