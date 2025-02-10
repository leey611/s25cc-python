# Make your terminal scroll
Let's make your terminal scroll or run infinitely with a `while` loop. The following shows the most minimal way to recreate a scroll art effect.

```
while True:
    print("hello")
```

It is scrolling, but the scroll doesn't seem obvious as it's printing the same thing, try:

```
i = 0
while True:
    print(i)
    i += 1
```

Now it seems more obvious that the task in the `while` loop is being run over and over again. Let's make the scroll a bit slower with `time.sleep`:

```
import time

while True:
    print(i)
    i += 1
    time.sleep(0.1)
```

We can now feel the scrolling, but we don't want the scroll to just show a single digit every line. We want it to look like a wallpaper that has a width:

```
while True:
    line = '@' * 50
    print(line)
    time.sleep(0.1)
```
Make it more dynamic with a `for` loop, `random`, `os` and conditionals:

```
import random, time, os

while True:
    line = ''
    width = os.get_terminal_size()[0] - 1
    for i in range(width):
        if random.randint(0, 10) < 5:
            line += "@"
        else:
            line = line + ' '
    print(line)
    time.sleep(0.1)
```

