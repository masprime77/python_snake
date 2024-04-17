import draw_row
import draw_map


def main():
    map_width = 21
    map_height = 23
    head_pos = [0, 0]
    food_pos = [10, 10]

    print("+" + "---" * (map_width - 2) + "+")

    draw_row.draw_row(map_width, map_height, "X", head_pos, "*", food_pos)

    print("+" + "---" * (map_width - 2) + "+")

    while True:
        draw_map.draw_map(map_width, map_height, head_pos, food_pos)


if __name__ == '__main__':
    main()
