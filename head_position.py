import os
import readchar


def head_position(map_width, map_height, head_pos):
    while True:
        k = readchar.readkey()
        # k = input("WASD/q")

        os.system("clear")

        if k == "q":
            exit(0)
        elif k == "w":
            head_pos[0] -= 1
            head_pos[0] %= map_height
        elif k == "d":
            head_pos[1] += 1
            head_pos[1] %= map_width
        elif k == "s":
            head_pos[0] += 1
            head_pos[0] %= map_height
        elif k == "a":
            head_pos[1] -= 1
            head_pos[1] %= map_width

        return head_pos
