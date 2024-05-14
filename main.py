import os
import time

import draw_map
import initial_screen


def main():
    map_width = 15
    map_height = 15
    head_pos = [0, 0]
    food_position = []
    points = 0
    tail_location = []

    os.system('clear')

    print("FELIZ CUMPLEAÑOS CHOLASOOOO!!!")
    time.sleep(1)
    print("TE AMO MUCHÍSIMO")
    time.sleep(1)
    print("ESPERO QUE TE GUSTE EL JUEGO")
    time.sleep(1)
    print("Usa WASD para moverte.\n"
          "Tienes que hacer 47 puntos!\n")
    input("Presiona ENTER para continuar...")

    initial_screen.initial_screen(map_width, map_height, head_pos)

    draw_map.draw_map(map_width, map_height, head_pos, food_position, points, tail_location)


def replay():
    map_width = 15
    map_height = 15
    head_pos = [0, 0]
    food_position = []
    points = 0
    tail_location = []

    os.system('clear')

    initial_screen.initial_screen(map_width, map_height, head_pos)

    draw_map.draw_map(map_width, map_height, head_pos, food_position, points, tail_location)


if __name__ == '__main__':
    main()  # Restructured git
