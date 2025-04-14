import tkinter as tk

# window
root = tk.Tk()
root.title("Phone Dialer")
root.geometry("300x400")

# dialed number string
dialed_number = tk.StringVar()

# display number text on top
display = tk.Entry(root, textvariable=dialed_number, font=("Helvetica", 24), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]

def press(key):
    current = dialed_number.get()
    dialed_number.set(current + key)

# btn1 = tk.Button(root, text='1', font=("Helvetica", 20), command=lambda: press('1'))
# btn1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# btn2 = tk.Button(root, text='2', font=("Helvetica", 20), command=lambda: press('2'))
# btn2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

# btn3 = tk.Button(root, text='3', font=("Helvetica", 20), command=lambda: press('3'))
# btn3.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

# create buttons
for index, label in enumerate(buttons):
    row = (index // 3) + 1  # start from row 1 because row 0 is display
    col = index % 3
    button = tk.Button(root, text=label, font=("Helvetica", 20), command=lambda l=label: press(l))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


# span grids 
for i in range(4):
    root.rowconfigure(i, weight=1) # weight=1 makes row or column to grow/stretch
for i in range(3):
    root.columnconfigure(i, weight=1)

root.mainloop()
