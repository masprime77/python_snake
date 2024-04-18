import draw_map
import initial_screen


def main():
    map_width = 8
    map_height = 8
    head_pos = [0, 0]
    food_position = []
    points = 0

    initial_screen.initial_screen(map_width, map_height, head_pos)

    draw_map.draw_map(map_width, map_height, head_pos, food_position, points)


if __name__ == '__main__':
    main()
