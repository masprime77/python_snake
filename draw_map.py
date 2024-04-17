import draw_row
import head_position


def draw_map(map_width, map_height, prev_head_pos, prev_food_pos):
    new_head_pos = head_position.head_position(map_width, map_height, prev_head_pos)

    print("+" + "---" * (map_width - 2) + "+")

    draw_row.draw_row(map_width, map_height, "X", new_head_pos, "*", prev_food_pos)

    print("+" + "---" * (map_width - 2) + "+")
