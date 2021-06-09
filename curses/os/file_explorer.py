import curses
import os


def go_back(stdstr):
    stdstr.clear()
    str1 = os.getcwd()
    current_dir = str1.split('/')
    current_dir.pop()
    separator = '/'
    directory = separator.join(current_dir)
    stdstr.refresh()
    
cwd = os.getcwd()
print((cwd))
# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")
#
# print("This file path, relative to os.getcwd()")
# print(__file__ + "\n")
#
# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")
#
# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")
#
# print("This file directory only")
# print(os.path.dirname(full_path))


def print_dir(stdscr, selected_row_idx):
    stdscr.clear()
    list_dir = os.listdir()
    cwd = os.getcwd()
    h, w = stdscr.getmaxyx()

    stdscr.addstr(0, 0, cwd)
    for idx, row in enumerate(list_dir):
        y = len(list_dir)//2 + idx
        x = 5
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0

    print_dir(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_UP and current_row_idx == 0:
            current_row_idx = len(list_dir) - 1
        elif key == curses.KEY_DOWN and current_row_idx < len(list_dir) - 1:
            current_row_idx += 1
        elif key == curses.KEY_DOWN and current_row_idx == len(list_dir) - 1:
            current_row_idx = 0
        elif key == curses.KEY_ENTER or key in [10, 13]:
            go_back()
        #     stdscr.getch()

        stdscr.refresh()


curses.wrapper(main)
