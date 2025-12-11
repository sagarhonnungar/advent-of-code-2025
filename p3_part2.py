
tot = 0

with open("input_p3.txt", "r") as f:
    banks = f.readlines()
    for b in banks:
        b = b.strip()
        num_bats_left = 12
        joltage = 0
        start_idx = 0
        while num_bats_left > 0:
            end_idx = len(b) - num_bats_left
            max_bat_joltage = b[start_idx]
            max_bat_idx = start_idx
            for i in range(start_idx, end_idx + 1):
                if b[i] > max_bat_joltage:
                    max_bat_joltage = b[i]
                    max_bat_idx = i

            joltage = joltage*10 + int(max_bat_joltage)
            start_idx = max_bat_idx + 1
            num_bats_left -= 1
            
        tot += joltage

print(tot)
