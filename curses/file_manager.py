## mpg123 (an mp3 audio player)
## is a dependency for this program.
## Make sure you install it before running.
import os
import curses
import time
import re

screen = curses.initscr()


def main(screen):
    ## Initial configuration
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    current_selection_index = 0
    sh, sw = screen.getmaxyx()

    ## Get path (change this when you run it)
    os.chdir("/home")

    ## Main loop for application
    while True:
        screen.clear()

        ## Strings always displayed on screen in main menu
        screen.addstr("CURRENT DIRECTORY: " + os.getcwd())
        screen.addstr(2, 0, "CONTENTS:")
        screen.addstr(sh - 1, 0, "Press ENTER to exit.")

        ## Creates list of directory contents, displays to screen
        for element in os.listdir():
            if os.listdir().index(element) == current_selection_index:
                screen.attron(curses.color_pair(1))
                screen.addstr(3 + os.listdir().index(element), 0, element)
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr(3 + os.listdir().index(element), 0, element)

        ## Block defining possible user actions
        ## and their outcomes.
        key = screen.getch()

        ## Enter breaks user out of the program
        if key == curses.KEY_ENTER or key in [10, 13]:
            break

        ## Up and down keys navigate the list
        elif key == curses.KEY_UP and current_selection_index != 0:
            current_selection_index -= 1
        elif key == curses.KEY_DOWN and current_selection_index != len(os.listdir()) - 1:
            current_selection_index += 1

        ## Left goes back a directory
        elif key == curses.KEY_LEFT:
            path_parent = os.path.dirname(os.getcwd())
            ## This line assures that the correct
            ## element will be selected
            ## when the user goes back a directory
            current_selection_index = os.listdir(path_parent).index(os.path.basename(os.getcwd()))
            os.chdir(path_parent)
        ## Right goes forward a directory,
        ## or plays a file using mpg123 if it's an mp3
        elif key == curses.KEY_RIGHT:
            if re.search(".mp3$", os.listdir()[current_selection_index]):
                screen.clear()
                ## Highligted text on first line of play screen
                top_text = "PLAYING: {0}".format(os.listdir()[current_selection_index])
                screen.attron(curses.color_pair(1))
                screen.addstr(0, sw // 2 - len(top_text) // 2, top_text)
                screen.attroff(curses.color_pair(1))

                ## Highligted text on second line of play screen
                ## Plus a couple blank lines
                next_text = "Press ^C to exit."
                screen.attron(curses.color_pair(2))
                screen.addstr(2, sw // 2 - len(next_text) // 2, next_text)
                screen.attroff(curses.color_pair(2))

                screen.refresh()

                ## This actually plays the track.
                os.system("mpg123 -q {0}".format(re.sub(" ", "\\ ", os.listdir()[current_selection_index])))
            else:
                os.chdir(os.listdir()[current_selection_index])
                current_selection_index = 0

        screen.refresh()


curses.wrapper(main)