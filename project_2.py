# Calculator
from tkinter import *
import tkinter.messagebox

app=Tk()
app.title('Calculator')

def myclick(number):
    entry.insert(END,number)

def clear():
    entry.delete(0,END)

def equal():
    try:
        output=eval(entry.get())
        output=str(output)
        entry.delete(0,END)
        entry.insert(END,output)
    except:
        tkinter.messagebox.showinfo('Error','Syntax Error')

frame=Frame(app,bg='skyblue',padx=10)
frame.pack()
entry=Entry(frame,relief=SUNKEN,borderwidth=3,width=30)
entry.grid(row=0,column=0,columnspan=3,ipady=2,pady=2)

btn_1=Button(frame,text='1',padx=15,pady=5,width=3,command=lambda: myclick(1))
btn_1.grid(row=1,column=0,pady=2)
btn_2=Button(frame,text='2',padx=15,pady=5,width=3,command=lambda: myclick(2))
btn_2.grid(row=1,column=1,pady=2)
btn_3=Button(frame,text='3',padx=15,pady=5,width=3,command=lambda: myclick(3))
btn_3.grid(row=1,column=2,pady=2)

btn_4=Button(frame,text='4',padx=15,pady=5,width=3,command=lambda: myclick(4))
btn_4.grid(row=2,column=0,pady=2)
btn_5=Button(frame,text='5',padx=15,pady=5,width=3,command=lambda: myclick(5))
btn_5.grid(row=2,column=1,pady=2)
btn_6=Button(frame,text='6',padx=15,pady=5,width=3,command=lambda: myclick(6))
btn_6.grid(row=2,column=2,pady=2)

btn_7=Button(frame,text='7',padx=15,pady=5,width=3,command=lambda: myclick(7))
btn_7.grid(row=3,column=0,pady=2)
btn_8=Button(frame,text='8',padx=15,pady=5,width=3,command=lambda: myclick(8))
btn_8.grid(row=3,column=1,pady=2)
btn_9=Button(frame,text='9',padx=15,pady=5,width=3,command=lambda: myclick(9))
btn_9.grid(row=3,column=2,pady=2)

btn_0=Button(frame,text='0',padx=15,pady=5,width=3,command=lambda: myclick(0))
btn_0.grid(row=4,column=1,pady=2)


btn_plus=Button(frame,text='+',padx=15,pady=5,width=3,command=lambda: myclick('+'))
btn_plus.grid(row=5,column=0,pady=2)
btn_min=Button(frame,text='-',padx=15,pady=5,width=3,command=lambda: myclick('-'))
btn_min.grid(row=5,column=1,pady=2)
btn_mul=Button(frame,text='*',padx=15,pady=5,width=3,command=lambda: myclick('*'))
btn_mul.grid(row=5,column=2,pady=2)

btn_div=Button(frame,text='/',padx=15,pady=5,width=3,command=lambda: myclick('/'))
btn_div.grid(row=6,column=0,pady=2)
btn_clear=Button(frame,text='clear',padx=15,pady=5,width=10,command=clear)
btn_clear.grid(row=6,column=1,columnspan=2,pady=2)

btn_equal=Button(frame,text='=',padx=15,pady=5,width=10,command=equal)
btn_equal.grid(row=7,column=0,columnspan=3,pady=2)

app.mainloop()