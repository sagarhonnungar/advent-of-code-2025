
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
        for b in buttons:
            b = b[1:-1].split(",")
            btn_bin = 0
            for pos in b:
                btn_bin |= (1 << int(pos))
            buttons_bin.append(btn_bin)

        def check_light_match(diagram, buttons, curr_res, i, curr_num_buttons, min_num_buttons):
            if i == len(buttons):
                return min_num_buttons

            min_num_buttons_1 = check_light_match(diagram, buttons, curr_res, i+1, curr_num_buttons, min_num_buttons)

            new_res = curr_res ^ buttons[i]
            curr_num_buttons += 1
            if new_res == diagram:
                if curr_num_buttons < min_num_buttons:
                    min_num_buttons = curr_num_buttons
            min_num_buttons_2 = check_light_match(diagram, buttons, new_res, i+1, curr_num_buttons, min_num_buttons)
            return min(min_num_buttons_1, min_num_buttons_2)

        min_num_buttons = check_light_match(light_diagram_bin, buttons_bin, 0, 0, 0, float('inf'))
        tot += min_num_buttons

print(tot)
            
