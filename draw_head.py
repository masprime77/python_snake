def draw_head(map_width, map_height, head, position):
    for y in range(map_height - 2):
        print("|", end="")
        for x in range(map_width - 2):
            if [y, x] == position:
                print(" " + head + " ", end="")
            else:
                print("   ", end="")

        print("|")
