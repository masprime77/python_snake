import os
import draw_head


def draw_map(map_width, map_height, head):
    os.system("clear")

    print("+--" + "---" * (map_width - 2) + "--+")

    head_pos = [10, 10]

    draw_head.draw_head(map_width, map_height, head, head_pos)

    print("+--" + "---" * (map_width - 2) + "--+")



