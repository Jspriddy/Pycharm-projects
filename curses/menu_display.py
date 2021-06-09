import curses
import time


def main(stdscr):
    curses.curs_set(0)
    # initialized but not activated
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    h, w = stdscr.getmaxyx()

    text = "Hello, World!"

    x = w//2 - len(text)//2
    y = h//2
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(5, 60, f"{y}/{x}")
    stdscr.attroff(curses.color_pair(1))

    stdscr.addstr(y, x, text)
    stdscr.addstr(25, 81, "Cruel world!")
    stdscr.addstr(26, 80, "This is one value down on the Y axis")
    stdscr.refresh()
    time.sleep(3)


curses.wrapper(main)
