import tkinter as tk

root = tk.Tk()
root.title("evil slider")
root.geometry("400x250")

label = tk.Label(root, text="slide to accept the terms and conditions", font=("Helvetica", 12))
label.pack(pady=20) #.pack() makes sure the element show

slider_value = tk.IntVar()

message_label = tk.Label(root, text="", font=("Helvetica", 12))
message_label.pack(pady=20)

def check_slider(value):
    if int(value) == 100:
        message_label.config(text="you agreed 😈")
        slider.config(state="disabled")  # disable the slider once hits 100

slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300,
                  variable=slider_value, showvalue=True, command=check_slider)
slider.pack()

root.mainloop()
