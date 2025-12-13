
split_ct = 0
with open("input_p7.txt", "r") as f:
    lines = f.readlines()
    lines = [list(l.strip()) for l in lines]
    for i in range(1, len(lines)):
        for j in range(len(lines[0])):
            if lines[i-1][j] == 'S':
                lines[i][j] = '|'
            elif lines[i-1][j] == '|':
                if lines[i][j] == '^':
                    if j>0:
                        lines[i][j-1] = '|'
                    if j<len(lines[0])-1:
                        lines[i][j+1] = '|'
                    split_ct += 1
                else:
                    lines[i][j] = '|'

print(split_ct)
