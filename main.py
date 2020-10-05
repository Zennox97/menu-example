# test_selection.py -- Provide example of moving through a menu

import curses

# menu index
menu        = ['SWAG', 'Play', 'Ranklist', 'Quit']
color_menu  = ['BLUE', 'RED', 'GREEN', 'YELLOW']



### Main menu ###
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)

    stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    BLUE    = curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    RED     = curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    GREEN   = curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    YELLOW  = curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)


    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:                # menu loop
        key = stdscr.getch()    # Collect next keyboard input

        stdscr.clear()          # Clear before doing anything

        if key == curses.KEY_UP and current_row_idx > 0:
            #stdscr.addstr(0,0,"Up arrow pressed! :D")
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) -1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            #stdscr.addstr(0,0,"ENTER!!!! :O")
            stdscr.clear()
            stdscr.addstr(0,0,"You pressed {}".format(menu[current_row_idx]))
            stdscr.refresh()
        elif key == curses.KEY_LEFT:
            stdscr.attron(curses.color_pair(2))

        print_menu(stdscr, current_row_idx)

    stdscr.refresh()

    
curses.wrapper(main)


