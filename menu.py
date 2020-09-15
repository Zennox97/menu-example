# menu.py -- Create a basic menu screen using python curses

import time
import curses

def main(stdscr):
    curses.curs_set(0)          # Remove blinking cursor
    
    h, w = stdscr.getmaxyx()    # How to find terminal dimentions
    
    text = "Hello, WORLD"

    x = w//2 - len(text)//2     # Formula(s) for finding middle of screen
    y = h//2                    # Use '//' to get integer value and not absolute

    stdscr.addstr(y, x, text)   
    stdscr.refresh()
    time.sleep(1)

curses.wrapper(main)            # Best way to execute menus


