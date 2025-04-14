import tkinter as tk
import random

root = tk.Tk()
root.title("moving button")
root.geometry("400x300")

# create button
button = tk.Button(root, text="Click Me!", font=("Helvetica", 16))
button.place(x=150, y=120)

def move_button(event):
    new_x = random.randint(0, 300)
    new_y = random.randint(0, 220)
    button.place(x=new_x, y=new_y)

# bind hover/enter event 
button.bind("<Enter>", move_button)

root.mainloop()
