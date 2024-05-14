import os
import readchar


def head_position(map_width, map_height, head_pos):
    while True:
        k = readchar.readkey()
        # k = input("WASD/q")

        os.system("clear")

        if k == "q":
            exit(0)
        elif k in ["w", "\x1b[A"]:
            head_pos[0] -= 1
            head_pos[0] %= map_height
        elif k in ["d", '\x1b[C']:
            head_pos[1] += 1
            head_pos[1] %= map_width
        elif k in ["s", '\x1b[B']:
            head_pos[0] += 1
            head_pos[0] %= map_height
        elif k in ["a", '\x1b[D']:
            head_pos[1] -= 1
            head_pos[1] %= map_width

        return head_pos
