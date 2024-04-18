import copy


def tail_location(prev_head_pos, points, tails):
    tails.append(copy.copy(prev_head_pos))

    while points != len(tails):
        tails.pop(0)

    return tails
