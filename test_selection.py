# test_selection.py -- Provide example of moving through a menu

import curses

def main(stdscr):
    curses.curs_set(0)

    while 1:                # menu loop
        key = stdscr.getch()    # Collect next keyboard input

        stdscr.clear()          # Clear before doing anything

        if key == curses.KEY_UP:
            stdscr.addstr(0,0,"Up arrow pressed! :D")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0,0,"DOWN arrow pressed? D:")
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"ENTER!!!! :O")

    stdscr.refresh()


curses.wrapper(main)


