import os

import main


def finish_game(cause):
    if cause == "in_tail":
        os.system("clear")
        print("YOU LOST!!!\n"
              "You touched your tail\n")

    action = " "

    while action not in ["Y", "N", "y", "n"]:
        action = input("Play again? (Y/N) ")

    if action.upper() == "Y":
        main.main()
    else:
        os.system("clear")
        exit()
