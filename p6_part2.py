
with open("input_p6.txt", "r") as f:
    lines = f.readlines()

    val_mat = []
    for l in lines[:-1]:
        vals = list(l.rstrip('\n'))
        val_mat.append(vals)

    ops = [o.strip() for o in lines[-1].strip().split()]

    results = []
    curr_prob_idx = 0
    curr_nums = []
    for j in range(len(val_mat[0])):
        num_str = "".join(val_mat[i][j] for i in range(len(val_mat))).replace(" ", "")
        if num_str == '':
            op = ops[curr_prob_idx]
            curr_prob_idx += 1
            if op == '+':
                res = sum(int(n) for n in curr_nums)
            elif op == '*':
                res = 1
                for n in curr_nums:
                    res *= int(n)
            results.append(res)
            curr_nums = []
        else:
            curr_nums.append(num_str)
    
    if curr_nums:
        op = ops[curr_prob_idx]
        if op == '+':
            res = sum(int(n) for n in curr_nums)
        elif op == '*':
            res = 1
            for n in curr_nums:
                res *= int(n)
        results.append(res)

    print(sum(results))

