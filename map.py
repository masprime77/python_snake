# Map dimensions
import os

MAP_WIDTH = 20
MAP_HEIGHT = 20

os.system("clear")

print("+--" + "---" * (MAP_WIDTH - 2) + "--+")

for i in range(MAP_HEIGHT):
    print("|  " + "   " * (MAP_WIDTH - 2) + "  |")

print("+--" + "---" * (MAP_WIDTH - 2) + "--+")
