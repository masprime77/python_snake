import readchar


def head_position(map_width, map_height, head_pos):
    while True:
        k = readchar.readkey()
        if k == "w":
            head_pos[0] -= 1
            head_pos[0] %= map_height - 2
            return head_pos

        if k == "d":
            head_pos[1] += 1
            head_pos[1] %= map_width - 2
            return head_pos

        if k == "s":
            head_pos[0] += 1
            head_pos[0] %= map_height - 2
            return head_pos

        if k == "a":
            head_pos[1] -= 1
            head_pos[1] %= map_width - 2
            return head_pos
