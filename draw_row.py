def draw_row(map_width, map_height, head, head_pos, food, food_location):
    for y in range(map_height):
        print("|", end="")
        for x in range(map_width):
            if [y, x] == head_pos:
                print(" " + head + " ", end="")
            elif [y, x] in food_location:
                print(" " + food + " ", end="")
            else:
                print("   ", end="")

        print("|")
