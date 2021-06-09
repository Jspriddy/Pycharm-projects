import curses
import time

stdscr = curses.initscr()

# # turns off blinking cursor
# curses.curs_set(0)
# # does not echo key input
# curses.noecho()
# # character break. does not require enter to be pressed
# curses.cbreak()
# # treats special keys as special values?
# stdscr.keypad(True)
# #             y, x, str
# stdscr.addstr(5, 5, "Hello world!")
#
# # implement previous operations on screen
# stdscr.refresh()
# time.sleep(3)
#
# # Overrides changed settings to terminal
# curses.curs_set(1)
# curses.echo()
# curses.nocbreak()
# stdscr.keypad(False)
# curses.endwin()


def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(15, 30, "Goodbye world!")
    stdscr.refresh()
    time.sleep(4)
    stdscr.addstr(17, 50, "Cruel world!")
    stdscr.refresh()
    time.sleep(1.5)


curses.wrapper(main)
