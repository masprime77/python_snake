import copy
import os
import random

import readchar

# Numeric constants
MAP_WIDTH = 8
MAP_HEIGHT = 8
FOOD_AMOUNT = 8

# Character constants
head = ">"
TAIL = "*"
TAIL_END = "S"
FOOD = "."


def main():
    head_position = [0, 0]
    tail_positions = []
    food_position = []
    points = 0

    initial_screen(head_position)
    draw_map(head_position, food_position, points, tail_positions)


def initial_screen(head_position):
    os.system("clear")

    score(0)
    print("+" + "---" * MAP_WIDTH + "+")
    draw_row(head_position, [0, 0], [0, 0])
    print("+" + "---" * MAP_WIDTH + "+")


def draw_map(old_head_position, food_positions, points, tail_positions):
    new_head_position = head_position_x_y(old_head_position)

    if new_head_position in tail_positions:
        finish_game("in_tail")

    points = pop_food(food_positions, new_head_position, points)

    while len(food_positions) != FOOD_AMOUNT:
        food_positions.append(generate_new_food_position(new_head_position, food_positions, tail_positions))

    score(points)

    print("+" + "---" * MAP_WIDTH + "+")

    draw_row(new_head_position, food_positions, tail_positions)

    print("+" + "---" * MAP_WIDTH + "+")

    tail_positions = new_tail_positions(old_head_position, points, tail_positions)

    draw_map(new_head_position, food_positions, points, tail_positions)


def draw_row(new_head_position, food_positions, tail_positions):
    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
            if [y, x] == new_head_position:
                print(" " + head + " ", end="")
            elif [y, x] in food_positions:
                print(" " + FOOD + " ", end="")
            elif len(tail_positions) > 0 and [y, x] == tail_positions[0]:
                print(" " + TAIL_END + " ", end="")
            elif [y, x] in tail_positions:
                print(" " + TAIL + " ", end="")

            else:
                print("   ", end="")

        print("|")


def head_position_x_y(old_head_position):
    while True:
        global head
        k = readchar.readkey()
        # k = input("WASD/q")  # To debug

        os.system("clear")

        if k == "q":
            exit(0)
        elif k in ["w", "\x1b[A"]:
            old_head_position[0] -= 1
            old_head_position[0] %= MAP_HEIGHT
            head = "^"
        elif k in ["d", '\x1b[C']:
            old_head_position[1] += 1
            old_head_position[1] %= MAP_WIDTH
            head = ">"
        elif k in ["s", '\x1b[B']:
            old_head_position[0] += 1
            old_head_position[0] %= MAP_HEIGHT
            head = "v"
        elif k in ["a", '\x1b[D']:
            old_head_position[1] -= 1
            old_head_position[1] %= MAP_WIDTH
            head = "<"

        return old_head_position


def generate_new_food_position(new_head_position, food_positions, tail_positions):
    new_food_position = [random.randint(0, MAP_HEIGHT - 1), random.randint(0, MAP_WIDTH - 1)]

    while (new_food_position == new_head_position) | (new_food_position in food_positions) | (new_food_position in
                                                                                              tail_positions):
        new_food_position = [random.randint(0, MAP_HEIGHT - 1), random.randint(0, MAP_WIDTH - 1)]

    return new_food_position


def pop_food(food_positions, new_head_position, points):
    for food in food_positions:
        if food == new_head_position:
            food_positions.pop(food_positions.index(food))
            points += 1

    return points


def new_tail_positions(old_head_position, points, tail_positions):
    tail_positions.append(copy.copy(old_head_position))

    while points != len(tail_positions):
        tail_positions.pop(0)

    return tail_positions


def score(points):
    print("SCORE: {}".format(points))


def finish_game(cause):
    if cause == "in_tail":
        os.system("clear")
        print("YOU LOST!!!\n"
              "You touched your tail\n")

    action = " "

    while action not in ["Y", "N", "y", "n"]:
        action = input("Play again? (Y/N) ")

    if action.upper() == "Y":
        main()
    else:
        os.system("clear")
        exit()


if __name__ == '__main__':
    main()
