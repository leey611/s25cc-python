# Basic graphs with matplotlib
An accessible chart should have: title, data, axis, and labels.
[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py)
[Plot Types](https://matplotlib.org/stable/plot_types/index.html)
[Tutorials](https://matplotlib.org/stable/tutorials/index.html)

## Bar Charts and Line charts

A basic bar chart:
```
import matplotlib.pyplot as plt

x = ["a", "b", "c", "d", "e"]
y = [10, 20, 25, 30, 40]

plt.bar(x, y, color='blue', label='Line Plot') # use plt.barh() for horizontal bars
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Bar Chart')
plt.legend()
plt.show()
```

Add more colors for a bar chart:
```
...
colors = ["red", "green", "blue", "orange", "purple"]
...
plt.bar(x, y, color=colors)
...
```

Change `plot.bar` to `plt.plot` to create a line chart:
```
import matplotlib.pyplot as plt

x = ["a", "b", "c", "d", "e"]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')
plt.legend()
plt.show()
```

Add more lines by adding lists of y values:
```
import matplotlib.pyplot as plt

x = ["a", "b", "c", "d", "e"]

y1 = [10, 20, 25, 30, 40]
y2 = [15, 25, 30, 35, 45]
y3 = [5, 15, 20, 25, 30]

plt.plot(x, y1, marker='o', linestyle='-', color='b', label='Line 1')
plt.plot(x, y2, marker='s', linestyle='--', color='r', label='Line 2')
plt.plot(x, y3, marker='^', linestyle='-.', color='g', label='Line 3')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.legend()
plt.show()
```

## Markers
- `.` : Point marker
- `,` : Pixel marker
- `o` : Circle
- `v` : Triangle down
- `^` : Triangle up
- `<` : Triangle left
- `>` : Triangle right
- `s` : Square
- `p` : Pentagon
- `*` : Star
- `h` : Hexagon 1
- `H` : Hexagon 2
- `+` : Plus sign
- `x` : X sign
- `D` : Diamond
- `d` : Thin diamond
- `|` : Vertical line
- `_` : Horizontal line

## Line Styles
- `'-'` : Solid line (default)
- `'--'` : Dashed line
- `'-.'` : Dash-dot line
- `':'` : Dotted line
- `''` (empty string) : No line (only markers will be shown)

## Colors
### Abbreviations
- `'b'` : Blue
- `'g'` : Green
- `'r'` : Red
- `'c'` : Cyan
- `'m'` : Magenta
- `'y'` : Yellow
- `'k'` : Black
- `'w'` : White

### Hex color codes
`'#ff0000'` 

### HTML color names
`'orange'`, `'purple'`, `'gold'`, `'lime'`, etc

### RGB or RGBA tuples:
`(1, 0, 0)` for red or `(1, 0, 0, 0.5)` for red with alpha

### Grayscale values:
A float between `0` and `1`, e.g., `'0.5'` for gray

## Scatter Plot
```
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
y = [5, 15, 10, 20, 18, 25, 30, 22, 28, 35]  

sizes = [value * 10 for value in y]  
colors = x  

plt.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7) #cmap stands for color map
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.colorbar(label="Color Scale")
plt.show()
```
## `cmap`: color map
### **Sequential (Good for Continuous Data)**
- `'plasma'` (Purple → Red → Yellow)
- `'inferno'` (Black → Orange → Yellow)
- `'magma'` (Black → Purple → Yellow)
- `'cividis'` (Blue → Yellow)

### **Diverging (Good for Positive/Negative Values)**
- `'coolwarm'` (Blue → White → Red)
- `'seismic'` (Blue → White → Red)

### **Categorical (For Distinct Groups)**
- `'tab10'` (10 distinct colors)
- `'Set3'` (Soft pastel colors)

## Subplots
```
import matplotlib.pyplot as plt

# Create a figure with 2 subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# First subplot (Bar chart)
ax[0].bar(['A', 'B', 'C'], [10, 20, 15], color='blue')
ax[0].set_title("Bar Chart")

# Second subplot (Line chart)
ax[1].plot([1, 2, 3], [5, 10, 15], marker='o', color='red')
ax[1].set_title("Line Chart")

plt.show()
```
## [More examples](https://matplotlib.org/stable/gallery/lines_bars_and_markers/index.html)