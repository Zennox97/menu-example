# menu.py -- Create a basic menu screen using python curses

import time
import curses

def main(stdscr):
    curses.curs_set(0)      # Remove blinking cursor
    
    h, w = stdscr.getmaxyx()
    
    text = "Hello, WORLD"

    x = w//2 - len(text)//2
    y = h//2

    stdscr.addstr(y, x, text)
    stdscr.refresh()
    time.sleep(1)

curses.wrapper(main)


