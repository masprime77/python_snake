import draw_head
import head_position


def draw_map(map_width, map_height, prev_head_pos):
    new_head_pos = head_position.head_position(map_width, map_height, prev_head_pos)

    print("+--" + "---" * (map_width - 2) + "--+")

    draw_head.draw_head(map_width, map_height, "X", new_head_pos)

    print("+--" + "---" * (map_width - 2) + "--+")
