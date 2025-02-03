# 01: Your first sketch
After setting up the Thonny Python Editor and the py5 Thonny plugin, run the code in `01_first_sketch.md`.

## Quick walk-through
- `size(400, 400)`: create a canvas with a 400px width and 400px height
- `circle(mouse_x, mouse_y, 10)`: draw a circle at the position of mouse (x and y); the size of the circle is 10px width and height; `circle(x_pos, y_pos, circle_size)`
- `def`: to define a function in Python, use the `def` keyword.
- Indentation: Python uses a 4-spaces indentation to indicate a block of code.
- Built-in variables: in py5, there are variables that you get for free, such as `mouse_x`, `mouse_y`, `width`, `height`.
 
```
def setup():
    size(400, 400) # sizing your canvas
    

def draw():
    circle(mouse_x, mouse_y, 10) # x position, y position, and size of a circle

run_sketch()
```

## `setup()` and `draw()`
Add `background("#0000ff")` after `size(400, 400)` as follows, and then run the sketch.
```
def setup():
    size(400, 400) # sizing your canvas
    background("#0000ff")
```

Comment out `background("#0000ff")` using # or remove it, and then add it before `circle(mouse_x, mouse_y, 10)`. 
```
def draw():
    background("#0000ff")
    circle(mouse_x, mouse_y, 10)
```
The difference between `setup()` and `draw()` is that `setup()` gets called once, and `draw()` gets called repeatedly/every frame. See the [docs](https://py5coding.org/content/user_functions.html).

## Order of code
If you put `background("#0000ff")` after `circle(mouse_x, mouse_y, 10)`, the circles aren't showning as the blue background covers the circles.
```
def draw():
    circle(mouse_x, mouse_y, 10)
    background("#0000ff")
```
**The code written later gets drawn later on the canvas**, so it is important to keep the order right while drawing.

## Notes on py5 modes
Sometimes you may see code in the docs or from AI tools being written in different ways, see [here](https://py5coding.org/content/py5_modes.html):
```
import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
```
The above style written with the `py5.` notation is called Module Mode, which is commonly used when using py5 with other Python modules together, such as `numpy`.

The style without the `py5.` notation is called Imported Mode.







