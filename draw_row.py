def draw_row(map_width, map_height, head, head_pos, food, food_pos):
    for y in range(map_height):
        print("|", end="")
        for x in range(map_width):
            if [y, x] == head_pos:
                print(" " + head + " ", end="")
            elif [y, x] == food_pos:
                print(" " + food + " ", end="")
            else:
                print("   ", end="")

        print("|")
