import draw_row


def initial_screen(map_width, map_height, head_pos, food_pos):
    print("+" + "---" * map_width + "+")

    draw_row.draw_row(map_width, map_height, "X", head_pos, " ", food_pos)

    print("+" + "---" * map_width + "+")