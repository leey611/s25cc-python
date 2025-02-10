# code reference: https://github.com/asweigart/scrollart/blob/main/python/starfield.py
# live demo: https://scrollart.org/starfield/

import random, time, os

DELAY = 0.02

def main():
    change_amount = 0.5
    density = 0.0
    while True:
        width = os.get_terminal_size()[0] - 1
        if density < 0 or density > 100:
            change_amount *= -1 # if the density is < 0 or > 100, reverse it 
        density = density + change_amount # updating the density of the starfield

        line = ''
        for i in range(width):
            if random.randint(0, 100) < density:
                line = line + '*' # append a char to a printed line
            else:
                line = line + ' ' # append a spapce to a printed line

        print(line); time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Starfield, by Al Sweigart al@inventwithpython.com 2022')