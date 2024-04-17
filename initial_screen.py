import os

import draw_row
import score


def initial_screen(map_width, map_height, head_pos):
    os.system("clear")

    score.score(0)

    print("+" + "---" * map_width + "+")

    draw_row.draw_row(map_width, map_height, "X", head_pos, " ", [5, 5])

    print("+" + "---" * map_width + "+")
