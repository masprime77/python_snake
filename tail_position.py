import copy


def tail_location(head_pos, points, tails):
    tails.append(copy.copy(head_pos))

    while points != len(tails):
        tails.pop(0)

    return tails
