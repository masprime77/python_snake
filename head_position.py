import readchar


def head_position(position):
    while True:
        k = readchar.readkey()
        if k == "w":
            position[0] -= 1
            return position

        if k == "d":
            position[1] += 1
            return position

        if k == "s":
            position[0] += 1
            return position

        if k == "a":
            position[1] -= 1
            return position
