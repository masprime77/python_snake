import copy
import os
import random

import readchar

MAP_WIDTH = 10
MAP_HEIGHT = 10


def main():
    head_position = [0, 0]
    tails_positions = []
    food_position = []
    points = 0

    initial_screen(head_position)

    draw_map(head_position, food_position, points, tails_positions)


def initial_screen(head_pos):
    os.system("clear")

    score(0)

    print("+" + "---" * MAP_WIDTH + "+")

    draw_row("X", head_pos, " ", [5, 5], " ", " ", [6, 6])

    print("+" + "---" * MAP_WIDTH + "+")


def draw_map(prev_head_pos, food_location, points, tail_location):
    new_head_pos = head_position_x_y(prev_head_pos)

    if new_head_pos in tail_location:
        finish_game("in_tail")

    new_points = pop_food(food_location, new_head_pos, points)

    points = new_points

    FOOD_CNT = 10

    while len(food_location) != FOOD_CNT:
        food_location.append(new_food_positions(new_head_pos, food_location, tail_location))

    score(points)

    print("+" + "---" * MAP_WIDTH + "+")

    draw_row("X", new_head_pos, ".", food_location, "*", "$", tail_location)

    print("+" + "---" * MAP_WIDTH + "+")

    tail_location = new_tail_positions(prev_head_pos, new_points, tail_location)

    draw_map(new_head_pos, food_location, points, tail_location)


def draw_row(head, head_pos, food, food_location, tail, tail_end, tail_location):
    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
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


def head_position_x_y(head_pos):
    while True:
        k = readchar.readkey()
        # k = input("WASD/q")  # To debug

        os.system("clear")

        if k == "q":
            exit(0)
        elif k in ["w", "\x1b[A"]:
            head_pos[0] -= 1
            head_pos[0] %= MAP_HEIGHT
        elif k in ["d", '\x1b[C']:
            head_pos[1] += 1
            head_pos[1] %= MAP_WIDTH
        elif k in ["s", '\x1b[B']:
            head_pos[0] += 1
            head_pos[0] %= MAP_HEIGHT
        elif k in ["a", '\x1b[D']:
            head_pos[1] -= 1
            head_pos[1] %= MAP_WIDTH

        return head_pos


def new_food_positions(head_pos, food_location, tail_pos):
    new_food_position = [random.randint(0, MAP_HEIGHT - 1), random.randint(0, MAP_WIDTH - 1)]

    while (new_food_position == head_pos) | (new_food_position in food_location) | (new_food_position in tail_pos):
        new_food_position = [random.randint(0, MAP_HEIGHT - 1), random.randint(0, MAP_WIDTH - 1)]

    return new_food_position


def pop_food(food_location, head_location, points):
    for food in food_location:
        if food == head_location:
            food_location.pop(food_location.index(food))
            points += 1

    return points


def new_tail_positions(head_pos, points, tails):
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
    main()
