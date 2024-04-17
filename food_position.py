import random


def food_position(map_width, map_height, food_pos, head_pos):
    new_food_position = [random.randint(0, map_height - 2), random.randint(0, map_width - 2)]
    while new_food_position == head_pos:
        new_food_position = [random.randint(0, map_height - 2), random.randint(0, map_width - 2)]

    return new_food_position
