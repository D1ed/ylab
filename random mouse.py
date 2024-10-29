import ctypes
import random
import time
import math
import win32gui

xmax = ctypes.windll.user32.GetSystemMetrics(0) 
ymax = ctypes.windll.user32.GetSystemMetrics(1)

def get_position():
    _, _, (x,y) = win32gui.GetCursorInfo()
    return (x,y)

def move_mouse(pos):
    x_pos, y_pos = pos
    x = int(65536 * x_pos / xmax + 1)
    y = int(65536 * y_pos / ymax + 1)
    return ctypes.windll.user32.mouse_event(32769, x, y, 0, 0)
move_mouse(1)
def start(t=30, min_speed=10, max_speed=500, x_bound=[0,xmax], y_bound=[0,ymax],
    p_break = 0.005, break_range = (10, 60), p_scroll = 0.01, scroll_range = (100, 1000)):

    def get_new_speed(min_val, max_val, val, delta=0.01):
        new_val = val + random.randrange(-1,2)*(max_val-min_val)*delta
        if new_val<min_val or new_val>max_val:
            return get_new_speed(min_val, max_val, val, delta)
        return new_val

    steps_per_second = 35.0 

    print('Started.')
    endtime = time.time() + int(t*60)

    # Initialize position, speed and direction
    pos = get_position()
    speed = min_speed + random.random()*(max_speed-min_speed)
    direction = 2*math.pi*random.random()
    inside_boundary = False
    right_clicked = False

    # Keep moving mouse until end time, or until right click
    while (not right_clicked) and (time.time() < endtime):
        if ctypes.windll.user32.GetKeyState(0x02) not in [0,1]:
            right_clicked = True

        time.sleep(1.0/steps_per_second)

        # Taking a break of random duration
        duration = random.randint(*break_range) # in unit of seconds
        break_endtime = time.time() + duration
        r = random.random()
        if (1-p_break) <= r < 1:
            # Keep checking for right click to exit loop
            while (not right_clicked) and (time.time() < break_endtime):
                if ctypes.windll.user32.GetKeyState(0x02) not in [0,1]:
                    right_clicked = True
                time.sleep(1.0/steps_per_second)
                time_left = break_endtime - time.time()
                print('Paused %d / %ds' % (time_left,duration) + ' '*50, end='\r')
            pos = get_position()
            print(' '*50, end='\r')

        # Random scroll
        r = random.random()
        lines = random.randint(*scroll_range)
        sign = random.random()
        sign = -1 if sign < 0.5 else 1
        if (1-p_scroll) <= r < 1:
            time.sleep(random.random())
            ctypes.windll.user32.mouse_event(2048, 0, 0, sign*lines, 0)
            time.sleep(random.random())
            pos = get_position()

        # Random move
        move_mouse(pos)

        time_left = endtime - time.time()
        print('Running (time left: %ds)' % time_left + ' '*50, end='\r')

        if (pos[0] in range(*x_bound)) and (pos[1] in range(*y_bound)):
            inside_boundary = True

        # Update position, speed and direction
        speed = get_new_speed(min_speed, max_speed, speed)
        direction+=random.randrange(-1,2)*math.pi/5.0*random.random()
        new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
               int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))
        # Once mouse position is inside boundary, new position must also be inside
        if inside_boundary:
            while new_pos[0] not in range(*x_bound) or new_pos[1] not in range(*y_bound):
                direction  = 2*math.pi*random.random()
                new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
                   int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))
        pos=new_pos
    print('Stopped.' + ' ' * 50)