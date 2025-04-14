import tkinter as tk
import random

# window
root = tk.Tk()
root.title("D20 Roller")
root.geometry("300x200")

# label
result_label = tk.Label(root, text="", font=("Helvetica", 48), width=2, borderwidth=2, relief="solid")
result_label.pack(pady=20)

# roll dice function
def roll_d20():
    roll = random.randint(1, 20)
    result_label.config(text=str(roll))

    if roll < 10:
        root.config(bg="white")
        result_label.config(bg="white", fg="black")
    else:
        root.config(bg="red")
        result_label.config(bg="red", fg="white")

# button with an event
roll_button = tk.Button(root, text="Roll!", font=("Helvetica", 16), command=roll_d20)
roll_button.pack(pady=10) # padding on the y direction

# main loop
root.mainloop()
