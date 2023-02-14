from tkinter import *
from tkinter import messagebox

 
def summ():
    var1 = int(e1.get())
    var2 = int(e2.get())
    messagebox.showinfo('Результат', str(var1+var2))






root = Tk()
root.geometry('500x300')
root.title('Калькулятор')

e1 = Entry(root, width=25, bg='gray', fg='white')
e1.pack()
e2 = Entry(root, width=25, bg='gray', fg='white')
e2.pack()


Button(root, text='+', width=5, height=2, command=summ).pack()

root.mainloop()