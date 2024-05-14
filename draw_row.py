def draw_row(map_width, map_height, head, head_pos, food, food_location, tail, tail_end, tail_location):
    for y in range(map_height):
        print("|", end="")
        for x in range(map_width):
            if [y, x] == head_pos:
                print(" " + head + " ", end="")
            elif [y, x] in food_location:
                print(" " + food + " ", end="")
            elif len(tail_location) > 0 and [y, x] == tail_location[0]:
                print(" " + tail_end + " ", end="")
            elif [y, x] in tail_location:
                print(" " + tail + " ", end="")

            else:
                print("   ", end="")

        print("|")
