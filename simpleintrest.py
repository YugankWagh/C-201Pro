from tkinter import *

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    output = (p * r * t) / 100
    output = round(output, 2)
   
    result_label = Label(result_frame, text=f"The simple interest is: {output}", font=("Calibri", 12))
    result_label.pack()

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x300")
window.config(bg="light blue")

heading_label = Label(window, text="Simple Interest Calculator", font=("Calibri", 18, "bold"))
heading_label.place(x=50, y=20)

principal_label = Label(window, text="Principal:", font=("Calibri", 12))
principal_label.place(x=50, y=60)
principal_entry = Entry(window, width=20)
principal_entry.place(x=150, y=60)

rate_label = Label(window, text="Rate of Interest:", font=("Calibri", 12))
rate_label.place(x=50, y=90)
rate_entry = Entry(window, width=20)
rate_entry.place(x=150, y=90)

time_label = Label(window, text="Time:", font=("Calibri", 12))
time_label.place(x=50, y=120)
time_entry = Entry(window, width=20)
time_entry.place(x=150, y=120)

calculate_button = Button(window, text="Calculate", font=("Calibri", 12), command=calculate_interest)
calculate_button.place(x=150, y=150)

result_frame = LabelFrame(window, text="Result", font=("Calibri", 12))
result_frame.place(x=50, y=180, width=300, height=100)

result_label = Label(result_frame, text="", font=("Calibri", 12))
result_label.pack()

window.mainloop()