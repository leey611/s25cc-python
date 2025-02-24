# Repeating patterns with loops

repeat with a loop and `range()`
```
from turtle import *

colors = ['blue', 'red', 'green'] 

for i in range(100):   
    c = colors[i % 3]
    color(c)
    forward(steps)
    right(60) # play around with a different angle value
        
mainloop()
```
working with `while` loop:
```
speed(0)
color("red")
fillcolor("yellow")

begin_fill()
while True:
    forward(200)
    left(102) # change a different angle value
    if abs(pos()) < 1: # use `abs(pos()) < 1` to determine if turtle is back at it home position
        break
end_fill()

mainloop()
```
playing with `circle`:

```
count = 5
angle = 360 / count
size = 100
for i in range(count):
    left(angle)
    circle(size) # try `circle(size - i * 10)`
```
working with nested loops:
```
count = 5
angle = 360 / count
size = 100
for i in range(count):
    left(angle)
    for j in range(count)
        circle(size - j * 10)
```
add more:
```
for i in range(count):
    left(angle)
    for j in range(count):
        circle(size - j * 10)

pencolor("blue")
pensize(2)
for i in range(6):
    left(360/6)
    for j in range(count):
        circle(size/2 + j * 5)

pencolor("red")
for i in range(3):
    left(360/3)
    for j in range(count):
        circle(size/2 - j * 5)
```
drawing a hexagon:

reference: Creative Coding in Python: 30+ Programming Projects in Art, Games, and More by Sheena Vaidyanathan 
```
# Pseudocode
# repeat 6 times the following:
    # move 100 steps forward
    # turn 60 degrees to the left
```
turning into python code:
```
for i in range(6):
    forward(100)
    left(60)
```
Repeat the hexagon with a nested loop
```
# Pseudocode
# repeat 36 times the following:
    # repeat 6 times the following:
        # move 100 steps forward
        # turn 60 degrees to the left
    # turn at 10 degrees to the right
```
turning into python code:
```
for n in range(36):
    # repeat 6 times - move forward and turn
    for i in range(6):
        forward(100)
        left(60)
    right(10) # add a turn
```
select a random color using `random` for each hexagon:
```
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
for n in range(36):
    color(random.choice(colors))
    # repeat 6 times - move forward and turn
    for i in range(6):
        forward(100)
        left(60)
    right(10) # add a turn
```

drawing waves:
```
from turtle import *
import math

# Wave parameters
amplitude = 10
frequency = 0.1
phase_shift = -math.pi / 2  # Smooth start at sine zero-crossing

# Function to draw a horizontal wave at a specific y-offset
def draw_wave(y_offset):
    penup()
    start_x = -300
    start_y = amplitude * math.sin(frequency * start_x + phase_shift) + y_offset
    goto(start_x, start_y)
    pendown()

    for x in range(start_x, 300):
        y = amplitude * math.sin(frequency * x + phase_shift) + y_offset
        goto(x, y)

# Draw the top wave
draw_wave(200)  # Shift up by 200 units

# Draw the bottom wave
draw_wave(-200)  # Shift down by 200 units
```
