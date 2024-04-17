import random


def food_positions(map_width, map_height, head_pos):
    new_food_position = [random.randint(0, map_height - 1), random.randint(0, map_width - 1)]

    while new_food_position == head_pos:
        new_food_position = [random.randint(0, map_height - 1), random.randint(0, map_width - 1)]

    return new_food_position
