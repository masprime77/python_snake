import draw_row
import finish_game
import food_position
import head_position
import pop_food
import score
import tail_position


def draw_map(map_width, map_height, prev_head_pos, food_location, points, tail_location):
    new_head_pos = head_position.head_position(map_width, map_height, prev_head_pos)

    if new_head_pos in tail_location:
        finish_game.finish_game("in_tail")

    new_points = pop_food.pop_food(food_location, new_head_pos, points)

    points = new_points

    if points == 47:
        finish_game.finish_game("hb_dad")

    FOOD_CNT = 10

    while len(food_location) != FOOD_CNT:
        food_location.append(food_position.food_positions(map_width, map_height, new_head_pos, food_location,
                                                          tail_location))

    score.score(points)

    print("+" + "---" * map_width + "+")

    draw_row.draw_row(map_width, map_height, "X", new_head_pos, ".", food_location, "*", "$",
                      tail_location)

    print("+" + "---" * map_width + "+")

    tail_location = tail_position.tail_location(prev_head_pos, new_points, tail_location)

    draw_map(map_width, map_height, new_head_pos, food_location, points, tail_location)
