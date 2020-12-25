from tkinter import *


kushu

canvas=Tk()

# canvas.geometry("200x190")

numbers = "1234567890-+="
numbers = list(numbers)

lbl = Label(canvas, text="CALCULATOR")
lbl.pack()

buttons = []
txt  = StringVar()
lblOutput = Label(canvas, textvariable=txt)
txt.set('')

lblOutput.pack(side = "top")

# number = ""

f1 = Frame(canvas, bg = 'red', height = 100)
f1.pack(fill = X)
f2 = Frame(canvas, bg = 'green', height = 100) 
f2.pack(fill = X)
f3 = Frame(canvas, bg = 'blue', height = 100)
f3.pack(fill = X)
f4 = Frame(canvas, bg = 'orange', height = 100)
f4.pack(fill = X)

# def button1_clicked():
#     txt.set("hjgjhg")
def button_clicked(e):
    if e == "del":
        txt.set("")
        return
    val = txt.get()
    if e == "=":
        txt.set(eval(val))
        return
    val = val + e
    txt.set(val)

btn1 = Button(f1, text = "1", bd = 5, width = 5, command = lambda: button_clicked("1"))
btn2 = Button(f1, text = "2", bd = 5, width = 5, command = lambda: button_clicked("2"))
btn3 = Button(f1, text = "3", bd = 5, width = 5, command = lambda: button_clicked("3"))
btn4 = Button(f1, text = "4", bd = 5, width = 5, command = lambda: button_clicked("4"))
btn5 = Button(f2, text = "5", bd = 5, width = 5, command = lambda: button_clicked("5"))
btn6 = Button(f2, text = "6", bd = 5, width = 5, command = lambda: button_clicked("6"))
btn7 = Button(f2, text = "7", bd = 5, width = 5, command = lambda: button_clicked("7"))
btn8 = Button(f2, text = "8", bd = 5, width = 5, command = lambda: button_clicked("8"))
btn9 = Button(f3, text = "9", bd = 5, width = 5, command = lambda: button_clicked("9"))
btn0 = Button(f3, text = "0", bd = 5, width = 5, command = lambda: button_clicked("0"))
btnplus = Button(f3, text = "+", bd = 5, width = 5, command = lambda: button_clicked("+"))
btnminus = Button(f3, text = "-", bd = 5, width = 5, command = lambda: button_clicked("-"))
btnmult = Button(f4, text = "*", bd = 5, width = 5, command = lambda: button_clicked("*"))
btndiv = Button(f4, text = "/", bd = 5, width = 5, command = lambda: button_clicked("/"))
btneq = Button(f4, text = "=", bd = 5, width = 5, command = lambda: button_clicked("="))
btndel = Button(f4, text = "del", bd = 5, width = 5, command = lambda: button_clicked("del"))

btn1.pack(side = "left")
btn2.pack(side = "left")
btn3.pack(side = "left")
btn4.pack(side = "left")
btn5.pack(side = "left")
btn6.pack(side = "left")
btn7.pack(side = "left")
btn8.pack(side = "left")
btn9.pack(side = "left")
btn0.pack(side = "left")
btnplus.pack(side = "left")
btnminus.pack(side = "left")
btnmult.pack(side = "left")
btndiv.pack(side = "left")
btneq.pack(side = "left")
btndel.pack(side = "left")


# btn1 = Button(canvas, text = "delete", bd = 5, command = canvas.destroy)
# btn2= Button(canvas, text = "delete", bd = 5, command = canvas.destroy)
# btn3 = Button(canvas, text = "delete", bd = 5, command = canvas.destroy)




# btn = Button(f1, text = "Kushagra", bd = 5, command = canvas.destroy)
# btn.pack(side = 'left')
# btn = Button(f1, text = "Kushagra2", bd = 5, command = canvas.destroy)
# btn.pack(side = 'left')

# btn1.pack(side = "left")
# btn2.pack(side = "left")
# btn3.pack(side = "left")

canvas.mainloop()

