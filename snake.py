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
    
    SNAKE = [[sh//2,sw//2-1],[sh//2,sw//2],[sh//2,sw//2+1]]
    DIRECTION = curses.KEY_RIGHT

    for y,x in SNAKE:
        stdscr.addstr(y,x,'#')

    stdscr.getch()






curses.wrapper(main)
