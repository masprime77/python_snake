def pop_food(food_location, head_location):
    for food in food_location:
        if food == head_location:
            food_location.pop(food_location.index(food))
