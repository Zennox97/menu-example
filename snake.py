import curses
from curses import textpad

def main(stdscr):
    curses.curs_set(0)  # Disable cursor
    stdscr.nodelay(1)   # Constant movement
    stdscr.timeout(150) # Time until constant movement

    # Set screen height & width
    sh, sw = stdscr.getmaxyx()
    # Create the 'game' table
    box = [[3,3],[sh-3, sw-3]]
    # Generate rectangle
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    SNAKE = [[sh//2,sw//2+1],[sh//2,sw//2],[sh//2,sw//2+1]]
    DIRECTION = curses.KEY_RIGHT

    # Print the snake on screen
    for y,x in SNAKE:
        stdscr.addstr(y,x,'#')



    while 1: #Infinite loop
        KEY = stdscr.getch()

        if KEY in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            DIRECTION = KEY

        head = SNAKE[0]

        if DIRECTION == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif DIRECTION == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif DIRECTION == curses.KEY_UP:
            new_head = [head[0]-1,head[1]]
        elif DIRECTION == curses.KEY_DOWN:
            new_head = [head[0]+1,head[1]]

        SNAKE.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '#')


        stdscr.addstr(SNAKE[-1][0], SNAKE[-1][1], ' ')
        SNAKE.pop()

        if (SNAKE[0][0] in [box[0][0], box[1][0]] or
            SNAKE[0][1] in [box[0][1], box[1][1]] or
            SNAKE[0] in SNAKE[1:]):
            msg = "GAME OVER!"
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break


        stdscr.refresh()


    stdscr.getch()






curses.wrapper(main)
