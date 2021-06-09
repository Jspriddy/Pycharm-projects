import curses

menu = ["Artist / Album", "Track"]
print(len(menu[0]))
print(len(menu[1]))


def main(stdscr):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h - 1, w // 2, f"{h}:{w}")
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(0, 0, (menu[0] + " " * 20 + menu[1]))
    stdscr.attroff(curses.color_pair(1))
    stdscr.getch()

curses.wrapper(main)
