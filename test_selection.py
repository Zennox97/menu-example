# test_selection.py -- Provide example of moving through a menu

import curses

menu = ['SWAG', 'Play', 'Ranklist', 'Quit']

def print_menu(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        stdscr.addstr(y,x,row)

    stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)

    print_menu(stdscr)

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


