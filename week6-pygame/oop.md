# What is Object-Oriented Programming (OOP)?
OOP is a programming style that enables you to organize your code and reuse it with `class` and `objects`.

## Why Object-Oriented Programming (OOP)?
So far we have been controlling the main character's behaviors using different functions, such as `yellow_handle_movement()` and `handle_bullets()`. This works well when we are controlling one thing, but what if we want to create multiple enemies in the game? It doesn't make sense to create functions to handle each enemy. 

Therefore, we need a way to create multiple objects that represent our enemies, and to be able to control each enemy object in an organized, readable style.

## Classes
[reference](https://www.w3schools.com/python/python_classes.asp)

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36) # initialize an object called p1 with the Person class

print(p1.name)
print(p1.age)
```

## Methods (functions) in a Class
```
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() # calling the myfunc() method on the p1 object
```

## Resources
- 🎥 [Python Object Oriented Programming (OOP) - For Beginners](https://www.youtube.com/watch?v=JeznW_7DlB0) by Tech With Tim
- 🎥 [What is Object-Oriented Programming (OOP)? - Processing Tutorial](https://www.youtube.com/watch?v=YcbcfkLzgvs) by The Coding Train