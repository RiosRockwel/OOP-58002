from tkinter import *

window = Tk()
window.title("The smallest number would be")
window.geometry("400x300+20+10")

def findSmallest():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfSmallest.set(min(L))

lbl1 = Label(window, text = "Input Number")
lbl1.grid(row=0, column=1, columnspan=2, sticky=EW)
lbl2 = Label(window, text = "Enter your first number:")
lbl2.grid(row=1, column = 0, sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.grid(row=1, column = 1)
lbl3 = Label(window, text = "Enter your second number:")
lbl3.grid(row=2, column=0, sticky=W)
conOfent3=StringVar()
ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.grid(row=2,column=1)
lbl4 = Label(window,text="Enter your third number:")
lbl4.grid(row=3,column =0, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.grid(row=3, column=1)

btn1 = Button(window,text = "Find the Smallest number",command=findSmallest)
btn1.grid(row=4, column = 1)
lbl5 = Label(window,text="The smallest number would be:")
lbl5.grid(row=5,column=0,sticky=W)
conOfSmallest = StringVar()
ent5 = Entry(window,bd=3,state="readonly",textvariable=conOfSmallest)
ent5.grid(row=5,column=1)


mainloop()