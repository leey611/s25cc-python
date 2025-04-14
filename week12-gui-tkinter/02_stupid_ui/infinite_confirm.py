import tkinter as tk

def show_confirm(level=1):
    confirm_window = tk.Toplevel()
    confirm_window.title(f"confirm Level {level}")
    confirm_window.geometry("300x100")

    label = tk.Label(confirm_window, text=f"are you sure? (Level {level})", font=("Helvetica", 12))
    label.pack(pady=10)

    confirm_button = tk.Button(confirm_window, text="yes", command=lambda: show_confirm(level + 1))
    confirm_button.pack()

    cancel_button = tk.Button(confirm_window, text="cancel", command=confirm_window.destroy)
    cancel_button.pack(pady=5)

root = tk.Tk()
root.title("infinite confirm")
root.geometry("300x200")

main_label = tk.Label(root, text="please confir!")
main_label.pack(pady=20)

main_button = tk.Button(root, text="confirm!", font=("Helvetica", 14), command=lambda: show_confirm(1))
main_button.pack(pady=10)

root.mainloop()
