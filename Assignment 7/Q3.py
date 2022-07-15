from tkinter import *

root = Tk()
root.title('Simple Calculator')
net=0
original=0
disp = Entry(root ,width=35, borderwidth=5)
disp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_funk(n):
    cur = disp.get()
    disp.delete(0,END)
    disp.insert(0,str(cur)+str(n))
def button_clear():
    disp.delete(0,END)

def calculate():
  question = disp.get()
  answer=eval(question)
  disp.delete(0,END)
  disp.insert(0,answer)
  

    
    

button_1 = Button(root, text = '1', padx=40,pady=20, command=lambda:button_funk(1))
button_2 = Button(root, text = '2', padx=40,pady=20, command=lambda:button_funk(2))
button_3 = Button(root, text = '3', padx=40,pady=20, command=lambda:button_funk(3))
button_4 = Button(root, text = '4', padx=40,pady=20, command=lambda:button_funk(4))
button_5 = Button(root, text = '5', padx=40,pady=20, command=lambda:button_funk(5))
button_6 = Button(root, text = '6', padx=40,pady=20, command=lambda:button_funk(6))
button_7 = Button(root, text = '7', padx=40,pady=20, command=lambda:button_funk(7))
button_8 = Button(root, text = '8', padx=40,pady=20, command=lambda:button_funk(8))
button_9 = Button(root, text = '9', padx=40,pady=20, command=lambda:button_funk(9))
button_0 = Button(root, text = '0', padx=40,pady=20, command=lambda:button_funk(0))
button_add = Button(root, text = '+', padx=40,pady=20, command=lambda:button_funk('+'))
button_cls = Button(root, text = '*', padx=30,pady=20, command=lambda:button_funk('*'))
button_equals = Button(root, text = '=', padx=120,pady=20, command=lambda:calculate())

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_cls.grid(row=4, column=2,columnspan=1)
button_equals.grid(row=5, column=0,columnspan=3)

root.mainloop()