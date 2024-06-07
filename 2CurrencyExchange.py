from tkinter import *
from tkinter.ttk import *

win = Tk()

def exchange():
    global Ent
    Eurlbl.config(text=str(Ent.get()))
    USDlbl.config(text=str(float(Ent.get())* 1.089))

Ent = Entry(win)
Ent.grid(row=0,column=0)

excbtn = Button(win,text="Exchange",command=exchange)
excbtn.grid(row=1,column=1)

EtDlbl = Label(win,text="Euro To USD")
EtDlbl.grid(row=0,column=1)

Eurlbl = Label(win,text="Euro: ")
Eurlbl.grid(row=1,column=0)

USDlbl = Label(win,text="USD: ")
USDlbl.grid(row=2,column=0)


win.geometry('200x200')
win.mainloop()
