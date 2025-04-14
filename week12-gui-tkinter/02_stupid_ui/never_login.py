import tkinter as tk

root = tk.Tk()
root.title("never login")
root.geometry("300x200")

# username label
tk.Label(root, text="username:").pack()
# username field
username_entry = tk.Entry(root)
username_entry.pack()

# password label
tk.Label(root, text="password:").pack()
# password field
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# login btn
login_button = tk.Button(root, text="login", font=("Helvetica", 12))
login_button.pack(pady=10)

# warning
warning_label = tk.Label(root, text="", fg="red") #fg for foreground color
warning_label.pack()

def auto_erase():
    username_entry.delete(0, tk.END) # delete chars .delete(start, end)
    password_entry.delete(0, tk.END)
    warning_label.config(text="re-enter your credentials...")
    root.after(2000, auto_erase)

root.after(2000, auto_erase) # delay 2 secs

root.mainloop()
