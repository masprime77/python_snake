import os
import draw_head
import head_position


def draw_map(map_width, map_height, head):
    os.system("clear")

    head_pos = head_position.head_position([0, 0])

    print("+--" + "---" * (map_width - 2) + "--+")

    draw_head.draw_head(map_width, map_height, head, head_pos)

    print("+--" + "---" * (map_width - 2) + "--+")



