import os


def draw_map(map_width, map_height):
    os.system("clear")

    print("+--" + "---" * (map_width - 2) + "--+")

    for i in range(map_height):
        print("|  " + "   " * (map_width - 2) + "  |")

    print("+--" + "---" * (map_width - 2) + "--+")


if __name__ == '__main__':
    draw_map(20, 20)
