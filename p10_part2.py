import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

tot = 0
with open("input_p10.txt", "r") as f:
    lines = f.readlines()

    for l in lines:
        # Sample line: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        inp = l.strip().split()
        light_diagram = inp[0][1:-1]
        buttons = inp[1:-1]
        joltage_reqs = inp[-1]

        light_diagram_bin = 0
        for i in range(len(light_diagram)):
            if light_diagram[i] == '#':
                light_diagram_bin |= (1 << i)

        buttons_bin = []
        buttons_list = []
        for b in buttons:
            b = b[1:-1].split(",")
            btn_bin = 0
            for pos in b:
                btn_bin |= (1 << int(pos))
            buttons_bin.append(btn_bin)
            buttons_list.append([int(v) for v in b])


        joltage_reqs = [int(v) for v in joltage_reqs[1:-1].split(",")]


        m, n = len(joltage_reqs), len(buttons_list)

        A = np.zeros((m, n))
        for i, b in enumerate(buttons_list):
            for bb in b:
                A[bb, i] = 1

        b = np.zeros(m)
        for i, j in enumerate(joltage_reqs):
            b[i] = j

        res = milp(
            c=np.ones(n),                            # minimize total presses
            constraints=LinearConstraint(A, b, b),   # A x == t  (lb==ub => equality)
            integrality=np.ones(n),                  # every variable integer
            bounds=Bounds(0, np.inf),                # non-negative
        )

        # print(res.fun)
        tot += int(res.fun)

print(tot)
            
