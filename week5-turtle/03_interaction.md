# Interactivity in Turtle
let make our turtle draw a flower wherever our mouse clicks on the screen!
```
def draw_flower():
    for i in range(5):
        circle(20)
        left(360/5)

draw_flower()
```
call this function with `onscreenclick`:

```
def draw_flower(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        circle(20)
        left(360/5)
onscreenclick(draw_flower)
```

modify the code to grow flowers with a stem:
```
def draw_flower(x, y):
    penup()
    goto(x, -150)
    pendown()
    goto(x, y)
    for i in range(5):
        circle(20)
        left(360/5)
onscreenclick(draw_flower)
```


