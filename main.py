import os

import draw_row
import draw_map
import initial_screen


def main():
    map_width = 10
    map_height = 10
    head_pos = [0, 0]
    food_position = []
    points = 0

    os.system("clear")

    initial_screen.initial_screen(map_width, map_height, head_pos)

    draw_map.draw_map(map_width, map_height, head_pos, food_position, points)


if __name__ == '__main__':
    main()
