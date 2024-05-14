def score(points):
    print("SCORE: {}/47".format(points))
    percentage = int(20 * points / 47)
    print("[" + ("#" * percentage) + (" " * (20 - percentage)) + "]")
