import os
import readchar


def head_position(map_width, map_height, head_pos):
    while True:
        k = readchar.readkey()

        os.system("clear")

        if k == "q":
            exit(0)
        elif k == "w":
            head_pos[0] -= 1
            head_pos[0] %= map_height - 2
        elif k == "d":
            head_pos[1] += 1
            head_pos[1] %= map_width - 2
        elif k == "s":
            head_pos[0] += 1
            head_pos[0] %= map_height - 2
        elif k == "a":
            head_pos[1] -= 1
            head_pos[1] %= map_width - 2

        return head_pos
