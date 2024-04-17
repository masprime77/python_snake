import draw_row
import draw_map
import initial_screen


def main():
    map_width = 19
    map_height = 21
    head_pos = [0, 0]
    food_pos = [10, 10]

    initial_screen.initial_screen(map_width, map_height, head_pos, food_pos)

    while True:
        draw_map.draw_map(map_width, map_height, head_pos, food_pos)


if __name__ == '__main__':
    main()
