import draw_row
import food_position
import head_position


def draw_map(map_width, map_height, prev_head_pos, prev_food_pos):
    new_head_pos = head_position.head_position(map_width, map_height, prev_head_pos)

    new_food_pos = food_position.food_position(map_width, map_height, [0, 0], new_head_pos)

    print("+" + "---" * (map_width - 2) + "+")

    draw_row.draw_row(map_width, map_height, "X", new_head_pos, "*", new_food_pos)

    print("+" + "---" * (map_width - 2) + "+")
