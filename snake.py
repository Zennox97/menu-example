import curses
from curses import textpad

def main(stdscr):
    curses.curs_set(0)  # Disable cursor

    # Set screen height & width
    sh, sw = stdscr.getmaxyx()
    # Create the 'game' table
    box = [[3,3],[sh-3, sw-3]]
    # Generate rectangle
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.refresh()
    stdscr.getch()






curses.wrapper(main)
