import curses
import time

stdscr = curses.initscr()
curses.curs_set(0)
begin_x = 20
begin_y = 7
height = 5
width = 40
win = curses.newwin(height, width, begin_y, begin_x)
stdscr.refresh()
time.sleep(3)
curses.endwin()
