# Turtle graphics basics
## Intro
```
from turtle import *

title("my first sketch") # customize the title of your turtle sketch window

forward(100) # make your turtle move forward for 100 units
left(90) # make your turtle turn left 90 degrees

mainloop() # make the screen stay when the drawing ends
```
Note that in Turtle's coordinate systems, `(0, 0)` is the center of the sketch window. The x axis grows from left to right. The y axis grows from bottom to top.
```
forward(100) # make your turtle move forward for 100 units
left(90) # make your turtle turn left 90 degrees
forward(100) # move forward for 100 units
```
finishing the square:
```
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

mainloop()
```
changing the cursor with `shape()`
- `shape('turtle')`

changing pen speed with `speed()`
- 0: Fastest (no animation, instant drawing)
- 1: Slowest speed
- 2-9: Increasing speed levels (2 is slow, 9 is fast)

changing pen size with `pensize(thickness)`

## colors: `bgcolor`, `pencolor`, `fillcolor`, `begin_fill`, and `end_fill`
setting a background color and a pen color:
```
bgcolor("lightblue") #set background color
pencolor("yellow") #set pen color

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

mainloop()
```

setting and filling colors:

```
bgcolor("lightblue")
pensize(2)
pencolor("yellow")
fillcolor("red") # set fill color

begin_fill() # start filling
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill() # end filling

mainloop()
```

refactor the code with a loop:
```
begin_fill() # start filling
for i in range(4):
    forward(100)
    left(90)
end_fill() # end filling
```

| Format                   | Example                        |
|--------------------------|--------------------------------|
| Named String             | `"blue"`, `"cyan"`, `"black"`  |
| Hex Code                 | `"#FF5733"`, `"#000000"`       |
| RGB Tuple (0-1)          | `(0.5, 0.3, 0.7)`              |

Use `colormode(255)` to enable 0-255 color values 
```
colormode(255)
bgcolor("lightblue")
pencolor(255, 255, 0)
```

## Moving the pen without drawing: `penup` and `pendown`, `goto`
let's move the pen and draw another square:
```
# lift the pen, move forward for 110 units, put the pen down
penup()
forward(110)
pendown()

# set pen color to blue, fill color to pink
color("blue")
fillcolor("pink")

# draw another square
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

refactor the code by defining a function:
```
def draw_square():
    for i in range(4):
        forward(100)
        left(90)
```
Note that your function must be defined before it is called.

```
speed(0)
pensize(2)
colormode(255)
bgcolor("lightblue")
pencolor(255, 255, 0)
fillcolor("red")

begin_fill()
draw_square()
end_fill()

# lift the pen, move forward for 110 units, put the pen down
penup()
forward(110) # or use `goto(x, y)` to go to a specific position
pendown()

# set pen color to blue, fill color to pink
color("blue")
fillcolor("pink")

# draw another square
begin_fill()
draw_square()
end_fill()

mainloop()
```
add a circle at a specified position:
```
penup()
goto(200, 200)
pendown()

circle(100)
```

## Use object-oriented turtle graphics
You can use `turtle` in an [object-oriented programming (OOP)](https://www.youtube.com/watch?v=YcbcfkLzgvs) style. By this way, you can have multiple turtles drawing on the screen!

[reference](https://hourofpython.trinket.io/a-visual-introduction-to-python#/multiple-turtles/tina-and-tommy-s-colors)
```
import turtle

tina = turtle.Turtle() # initialize a turtle called tina
tina.shape('turtle') # set tina's shape
tina.color('black') # set tina's color

tina.left(90)
tina.forward(100)
tina.write("I'm Tina!")
tina.forward(20)
tina.right(90)

tommy = turtle.Turtle() # initialize a turtle called tommy
tommy.shape('turtle')
tommy.color('black')

tommy.right(90)
tommy.forward(100)
tommy.write("I'm Tommy!")
tommy.forward(20)
tommy.left(90)
```




