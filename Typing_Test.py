import curses
from curses import wrapper
import time
import random
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome To Typing test")
    stdscr.addstr("\nPress Any Key To Start")
    stdscr.refresh()
    stdscr.getkey()
def load_text():
    with open("target.txt","r") as FILE:
        lines = FILE.readlines()
        return random.choice(lines).strip()
def displaytext(stdscr, target, current,wpm,accuracy):
    stdscr.addstr(0, 0, target)
    stdscr.addstr(1,0,f"WPM- {wpm}")
    stdscr.addstr(1,13,f"ACCURACY- {accuracy}%")

    for i, char in enumerate(current):
        if i < len(target) and char == target[i]:
            color = curses.color_pair(1)  # correct
        else:
            color = curses.color_pair(2)  # wrong

        stdscr.addstr(0, i, char, color)

def test(stdscr):
    target = load_text()
    current = []
    wpm =0
    total_keystrokes = 0
    correct_keystrokes = 0

    
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        #______________WPM Calc______________
        time_elapse = max(time.time()-start_time,1)
        wpm = round((len(current)/5)/(time_elapse/60))

        #_____ACCURACY CALCULATION______
        accuracy = round((correct_keystrokes / total_keystrokes) * 100) if total_keystrokes else 100
        #_____________________________

        stdscr.clear()
        displaytext(stdscr,target,current,wpm,accuracy)
        stdscr.refresh()

        if "".join(current) == target:
            stdscr.nodelay(False)
            return wpm, accuracy
        try:
            key = stdscr.getkey()
        except curses.error:
            continue
        
        if  key == "\x1b": #ESC
            return None
        elif key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if current:
                current.pop()

        elif len(key) == 1 and len(current) < len(target):
            total_keystrokes += 1

            if key == target[len(current)]:
                correct_keystrokes += 1

            current.append(key)



def main(stdscr):
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_RED)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
    start_screen(stdscr)
    while True:
        result = test(stdscr)

        if result is None:
            break

        final_wpm, final_accuracy = result

        stdscr.clear()
        stdscr.addstr(1, 0, "Completed!")
        stdscr.addstr(3, 0, f"Final WPM: {final_wpm}")
        stdscr.addstr(4, 0, f"Final Accuracy: {final_accuracy}%")
        stdscr.addstr(6, 0, "Press any key to restart")
        stdscr.addstr(7, 0, "Press ESC to exit")
        stdscr.refresh()

        key = stdscr.getkey()
        if key == "\x1b":
            break

       
wrapper(main)