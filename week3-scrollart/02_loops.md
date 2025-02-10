# `for` loop and `while` loop
Loop is a way to execute a task multiple times, to run a block of code repeatedly, without writing the same code over and over again.

## `for` loops
`for` loop can be used to iterate through a list of items:
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
to perform a task multiple times on a given range:
```
for x in range(6):
    print(x)
```

## `while` loops
`while` loops execute a task or a block of code continuously if a condition is true.

The following code is an `if` statement that would execute a block of code once if a condition is true
```
count = 0
if count < 6:
    print(count)
```
Using `while` instead of `if` for the condition, the task is executed infinitely:

```
count = 0
while count < 6:
    print(count)
```
This means the program is stuck in the `while` loop! To stop the program, hit `ctrl + c` 

In order to prevent our program from being stuck in a loop, we need to make the condition become false by incrementing the `count`:

```
count = 0
while count < 6:
    print(count)
    count += 1 #same as count = count + 1
```

## References
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [while and for Loops](https://www.youtube.com/watch?v=cnRD9o6odjk) by The Coding Train
- [While Loop - Creative Coding with p5.js](https://www.youtube.com/watch?v=FyB_K-yC9yo) by Patt Vira
