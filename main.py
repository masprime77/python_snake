import draw_head
import draw_map


def main():
    map_width = 21
    map_height = 23
    head_pos = [0, 0]

    print("+" + "---" * (map_width - 2) + "+")

    draw_head.draw_head(map_width, map_height, "X", head_pos)

    print("+" + "---" * (map_width - 2) + "+")

    while True:
        draw_map.draw_map(map_width, map_height, head_pos)


if __name__ == '__main__':
    main()
