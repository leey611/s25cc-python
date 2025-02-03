# 05: function
Each bear is drawn inside the nested loop in the following code. Currently, the code doesn't look too bad, but we can make it more organized and readable by making a function.

```
def setup():
    size(400, 400) 

def draw():
    for column in range(6):
        for row in range(6):
            x_pos = column * 80
            y_pos = row * 80
            circle(x_pos - 20, y_pos - 20, 30)
            circle(x_pos + 20, y_pos - 20, 30)
            circle(x_pos, y_pos, 50)

run_sketch()
```

- [Python Functions](https://www.w3schools.com/python/python_functions.asp)