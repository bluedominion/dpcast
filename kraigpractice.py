#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()

window.title("Welcome to Kraig's app")

window.geometry('350x200')

def clicked():
    messagebox.showinfo('Message Title','Message Content')

btn = Button(window,text='Touch Me!', command=clicked)
btn.grid(column=0, row=0)

#Scrolling text box
#txt=scrolledtext.ScrolledText(window, width=40, height=10)
#txt.grid(column=0, row=0)

#Radio button silliness
#selected = IntVar()
#rad1 = Radiobutton(window, text="Ellen", value=1, variable=selected)
#rad2 = Radiobutton(window, text="Kraid", value=2, variable=selected)
#rad3 = Radiobutton(window, text="Dita", value=3, variable=selected)
#rad1.grid(column=0, row=0)
#rad2.grid(column=1, row=0)
#rad3.grid(column=2, row=0)

#def clicked():
#    print(str(selected.get())+" touched me!")
#btn = Button(window, text="Touch me!", command=clicked)
#btn.grid(column=3, row=0)

#check buttons!
#chk_state = BooleanVar()
#chk_state.set(True)
#chk = Checkbutton(window, text="Choose", var=chk_state)
#chk.grid(column=0, row=0)

#drop-down window!
#combo = Combobox(window)
#combo['values']=(1,2,3,4,5,"Text")
#combo.current(1)
#combo.grid(column=0, row=0)

#text entry field with click button and silly text!
#txt = Entry(window, width=10)
#txt.grid(column=1, row=0)
#def clicked():
#    res = txt.get() + " touched me!"
#    lbl.configure(text=res)

#lbl = Label(window, text="Hello", font=("ArialBold", 20))
#lbl.grid(column=0, row=0)

#def clicked():
#    lbl.configure(text="You touched me!")

#btn = Button(window, text="Click Me!", bg="green", fg="yellow", command=clicked)
#btn.grid(column=2,row=0)




window.mainloop()
