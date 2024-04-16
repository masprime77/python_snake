# Map dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 20

print("+--" + "---" * (MAP_WIDTH - 2) + "--+")

for i in range(MAP_HEIGHT):
    print("|  " + "   " * (MAP_WIDTH - 2) + "  |")

print("+--" + "---" * (MAP_WIDTH - 2) + "--+")
