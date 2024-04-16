import os


def draw_map(map_width, map_height, char_to_print):
    os.system("clear")

    print("+--" + "---" * (map_width - 2) + "--+")

    draw_char(map_width, map_height, char_to_print)

    print("+--" + "---" * (map_width - 2) + "--+")


def draw_char(map_width, map_height, char_to_print):
    for i in range(map_height - 2):
        print("|  ", end="")
        for j in range(map_width - 2):
            print(" " + char_to_print + " ", end="")

        print("  |")


if __name__ == '__main__':
    draw_map(21, 23, " ")
