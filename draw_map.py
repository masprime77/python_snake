import draw_row
import food_position
import head_position
import pop_food


def draw_map(map_width, map_height, prev_head_pos, food_location):
    new_head_pos = head_position.head_position(map_width, map_height, prev_head_pos)

    pop_food.pop_food(food_location, new_head_pos)

    FOOD_CNT = 10

    while len(food_location) != FOOD_CNT:
        food_location.append(food_position.food_positions(map_width, map_height, new_head_pos, food_location))

    print("+" + "---" * map_width + "+")

    draw_row.draw_row(map_width, map_height, "X", new_head_pos, "*", food_location)

    print("+" + "---" * map_width + "+")
