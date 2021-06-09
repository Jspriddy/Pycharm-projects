import unicurses
from unicurses import *


def main():

    stdscr = initscr()

    mvaddstr(5, 30, "Hello World!")
    getch()

    endwin()

    return 0


if __name__ == "__main__":
    main()