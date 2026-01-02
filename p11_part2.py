# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
from collections import defaultdict
outputs = defaultdict(list)
start = "svr"
with open("input_p11.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        parts = l.strip().split(": ")
        key = parts[0]
        values = parts[1].split()
        for v in values:
            outputs[key].append(v)

num_paths = 0
memo = {}
def count_paths_with_dac_and_fft(node):
    if node == "out":
        return 0, 0, 0, 1 # both dac and fft, only dac, only fft, neither
    if node in memo:
        return memo[node]
    out1, out2, out3, out4 = 0, 0, 0, 0
    for neighbor in outputs[node]:
        curr_out1, curr_out2, curr_out3, curr_out4 = count_paths_with_dac_and_fft(neighbor)
        if node == "dac":
            out1 += curr_out1 + curr_out3
            out2 += curr_out2 + curr_out4
            out3 += 0
            out4 += curr_out4
        elif node == "fft":
            out1 += curr_out1 + curr_out2
            out2 += 0
            out3 += curr_out3 + curr_out4
            out4 += curr_out4
        else:
            out1 += curr_out1
            out2 += curr_out2
            out3 += curr_out3
            out4 += curr_out4
    memo[node] = (out1, out2, out3, out4)
    return out1, out2, out3, out4

num_paths_with_dac_and_fft, num_paths_with_dac_only, num_paths_with_fft_only, num_paths_with_neither = count_paths_with_dac_and_fft(start)
print(num_paths_with_dac_and_fft)
