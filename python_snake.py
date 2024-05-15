import copy
import os
import random

import readchar


def main():
    map_width = 10
    map_height = 10
    head_pos = [0, 0]
    food_position = []
    points = 0
    tail_location = []

    initial_screen(map_width, map_height, head_pos)

    draw_map(map_width, map_height, head_pos, food_position, points, tail_location)


def initial_screen(map_width, map_height, head_pos):
    os.system("clear")

    score(0)

    print("+" + "---" * map_width + "+")

    draw_row(map_width, map_height, "X", head_pos, " ", [5, 5], " ", " ", [6, 6])

    print("+" + "---" * map_width + "+")


def draw_map(map_width, map_height, prev_head_pos, food_location, points, tail_location):
    new_head_pos = head_position(map_width, map_height, prev_head_pos)

    if new_head_pos in tail_location:
        finish_game("in_tail")

    new_points = pop_food(food_location, new_head_pos, points)

    points = new_points

    FOOD_CNT = 10

    while len(food_location) != FOOD_CNT:
        food_location.append(food_positions(map_width, map_height, new_head_pos, food_location, tail_location))

    score(points)

    print("+" + "---" * map_width + "+")

    draw_row(map_width, map_height, "X", new_head_pos, ".", food_location, "*", "$", tail_location)

    print("+" + "---" * map_width + "+")

    tail_location = tail_positions(prev_head_pos, new_points, tail_location)

    draw_map(map_width, map_height, new_head_pos, food_location, points, tail_location)


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


def head_position(map_width, map_height, head_pos):
    while True:
        k = readchar.readkey()
        # k = input("WASD/q")

        os.system("clear")

        if k == "q":
            exit(0)
        elif k in ["w", "\x1b[A"]:
            head_pos[0] -= 1
            head_pos[0] %= map_height
        elif k in ["d", '\x1b[C']:
            head_pos[1] += 1
            head_pos[1] %= map_width
        elif k in ["s", '\x1b[B']:
            head_pos[0] += 1
            head_pos[0] %= map_height
        elif k in ["a", '\x1b[D']:
            head_pos[1] -= 1
            head_pos[1] %= map_width

        return head_pos


def food_positions(map_width, map_height, head_pos, food_location, tail_pos):
    new_food_position = [random.randint(0, map_height - 1), random.randint(0, map_width - 1)]

    while (new_food_position == head_pos) | (new_food_position in food_location) | (new_food_position in tail_pos):
        new_food_position = [random.randint(0, map_height - 1), random.randint(0, map_width - 1)]

    return new_food_position


def pop_food(food_location, head_location, points):
    for food in food_location:
        if food == head_location:
            food_location.pop(food_location.index(food))
            points += 1

    return points


def tail_positions(head_pos, points, tails):
    tails.append(copy.copy(head_pos))

    while points != len(tails):
        tails.pop(0)

    return tails


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
    main()  # Restructured git
