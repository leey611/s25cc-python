# code reference: https://github.com/asweigart/scrollart/blob/main/python/thorns.py
# live demo: https://scrollart.org/thorns/

import random, math, os, time

WIDTH = os.get_terminal_size()[0]
DELAY = 0.005
THORN_CHAR = '-'

LEVELS = [1, 1, 1, 1, 1, 1, 1, 3, 6]
MULTIPLIER = 10

try:
    while True:
        line_length = int(random.choice(LEVELS) * ((random.random() + 1) * MULTIPLIER))
        line = THORN_CHAR * line_length
        
        if len(line) > WIDTH:
            line = THORN_CHAR * WIDTH # if the length exceeds the WIDTH, make it equal to WIDTH 

        print(line.center(WIDTH)) # align the line in the center of the WIDTH
        time.sleep(DELAY)
        
except KeyboardInterrupt:
    print('Thorns, by Al Sweigart al@inventwithpython.com 2024')