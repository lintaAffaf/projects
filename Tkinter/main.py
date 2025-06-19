import tkinter
from tkinter import Button, Entry, Label

from playground import calculate

window=tkinter.Tk()
window.title("miles to km converter")
window.minsize(width=500,height=400)
window.config(padx=50,pady=50)

# def button_clicked():
#     print("i got clicked")
#     my_label.config(text=input.get())
#
# my_label=tkinter.Label(text="text",font=("Arial",24,"bold"))
# my_label.grid(column=0,row=0)
# # my_label.config(padx=30,pady=30)
#
# button= Button(text="click me",command=button_clicked)
# button.grid(column=1,row=1)
#
# newbutton=Button(text="new button")
# newbutton.grid(column=2,row=0)
#
# input= Entry(width=10)
# input.grid(column=3,row=2)
def button_clicked():
    miles=float(input.get())
    answer.config(text=miles*1.6)
input=Entry(width=10)
input.grid(column=1,row=0)

miles=Label(text="miles")
miles.grid(column=2,row=0)
miles.config(padx=10,pady=10)

km=Label(text="km")
km.grid(column=2,row=1)
km.config(padx=10,pady=10)

equalto=Label(text="is equal to")
equalto.grid(column=0,row=1)

answer=Label(text="0")
answer.grid(column=1,row=1)

calculate=Button(text="calculate",command=button_clicked)
calculate.grid(column=1,row=2)
calculate.config(padx=5,pady=5)



window.mainloop()