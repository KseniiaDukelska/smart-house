import tkinter as tk
import time

root = tk.Tk()

root.title("Dukelska K.B.")
root.geometry("680x560")

Counter = tk.IntVar()
Counter.set(0)
State = False
M = 13
N = 66

lbl1 = tk.Label(root, text="State = {} ".format(State), font=("Arial", 14))
lbl1.grid(row=3, column=1)
label1 = tk.Label(root, text='Counter={}'.format(Counter.get()), font=("Arial", 14))
label1.grid(row=1, column=1)
label2 = tk.Label(root, text='Enter number M', font=("Arial", 14))
label2.grid(row=4, column=1)

txt = tk.Entry(root, width=20)
txt.grid(row=5, column=1)

res = "{}".format(txt.get())


def entry(str):
    global M
    global Counter
    current_time = time.strftime("%H:%M:%S")
    if txt.get().isdigit():
        listbox.insert(tk.END, f"Set to {txt.get()} with Entry at {current_time}")
        M=int(txt.get())
        if int(txt.get())<=Counter.get():
            label1.config(bg='red')
        else:
            label1.config(bg='white')


txt.bind("<Return>", entry)


def clicked():
    global Counter
    global N
    global M
    if Counter.get() < N:
        Counter.set(Counter.get() + 1)
        current_time = time.strftime("%H:%M:%S")
        listbox.insert(tk.END, f"Grow with button on 1, current: {Counter.get()} at {current_time}")
    else:
        Counter.set(Counter.get() + 0)
        label1.config(bg='white')
    if Counter.get() >= M:
        label1.config(bg='red')
    else:
        label1.config(bg='white')
    label1.config(text='Counter={}'.format(Counter.get()))

    global State
    State = not State
    lbl1.config(text='State= {}'.format(State))


scal = tk.Scale(root, orient=tk.HORIZONTAL, length=300, from_=0, to=N, tickinterval=4, resolution=4)
scal.grid(row=3, column=1)


def scalFunc(str):
    global Counter
    Counter.set(scal.get())
    current_time = time.strftime("%H:%M:%S")
    listbox.insert(tk.END, f"Grow up with scal, current: {Counter.get()} at {current_time}")
    label1.config(text='Counter={}'.format(Counter.get()))
    if scal.get() >= M:
        label1.config(bg='red')
    else:
        label1.config(bg='white')
    


scal.bind("<B1-Motion>", scalFunc)


btn = tk.Button(root, text='Grow', bg='red',font=("Arial Bold", 14), command=clicked)
btn.grid(row=2, column=1)

label3 = tk.Label(root, text='Events', font=("Arial", 14))
label3.grid(row=6, column=1)
listbox = tk.Listbox(root, width=50, height=20)
listbox.grid(row=7, column=1)


root.mainloop()
