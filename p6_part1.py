
with open("input_p6.txt", "r") as f:
    lines = f.readlines()

    val_mat = []
    for l in lines[:-1]:
        vals = [int(v) for v in l.strip().split()]
        val_mat.append(vals)

    ops = [o.strip() for o in lines[-1].strip().split()]

    results = []
    for j in range(len(val_mat[0])):
        op = ops[j]
        if op == '+':
            res = sum(val_mat[i][j] for i in range(len(val_mat)))
        elif op == '*':
            res = 1
            for i in range(len(val_mat)):
                res *= val_mat[i][j]
        results.append(res)

    print(sum(results))

