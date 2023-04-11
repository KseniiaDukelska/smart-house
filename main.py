from tkinter import*
from tkinter.messagebox import showinfo

window = Tk()

window.title("Dukelska K.B.")
window.geometry("680x560")

Counter = 0
State = False
M = 13
N = 66

lbl1 = Label(window, text="State = {} ".format(State), font=("Arial", 14))
lbl1.grid(row=3, column=1)
label1 = Label(window, text='Counter={}'.format(Counter), font=("Arial", 14))
label1.grid(row=1, column=1)
label2 = Label(window, text='Enter number M', font=("Arial", 14))
label2.grid(row=4, column=1)

txt = Entry(window, width=20)
txt.grid(row=5, column=1)

res = "{}".format(txt.get())


def func2(str):
    global M
    global Counter
    if txt.get().isdigit():
        M=int(txt.get())
        if int(txt.get())<=Counter:
            label1.config(bg='red')
        else:
            label1.config(bg='white')


txt.bind("<Return>", func2)


def clicked():
    global Counter
    global N
    global M
    if Counter < N:
        Counter += 1
    else:
        Counter = 0
        label1.config(bg='white')
    if Counter >= M:
        label1.config(bg='red')
    else:
        label1.config(bg='white')
    label1.config(text='Counter={}'.format(Counter))

    global State
    State = not State
    lbl1.config(text='State= {}'.format(State))


scal = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=N, tickinterval=4, resolution=4)
scal.grid(row=3, column=2)


def func1(str):
    global Counter
    Counter = scal.get()
    label1.config(text='Counter={}'.format(Counter))
    if scal.get() >= M:
        label1.config(bg='red')
    else:
        label1.config(bg='white')
    


scal.bind("<B1-Motion>", func1)


btn = Button(window, text='Grow', bg='red',font=("Arial Bold", 14), command=clicked)
btn.grid(row=2, column=1)

langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = Tk.Variable(value=langs)

listbox = Tk.Listbox(
    window,
    listvariable=var,
    height=6,
    selectmode=Tk.EXTENDED
)

listbox.pack(expand=True, fill=Tk.BOTH)


def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)
window.mainloop()
