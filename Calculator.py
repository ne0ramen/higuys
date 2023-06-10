from tkinter import *

def button_press(num):
    global equation_text

    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def clear():
    global equation_text
    
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable = equation_label, font =("consolas", 20), bg = "white", width = 24, height = 2)
label.pack()

frame = Frame(window)
frame.pack()

btns = []
btns_num = -1

for x in range(3):
    for y in range(3):
        btns_num += 1
        btns.append(Button(frame,text=btns_num+1, height=4, width=9, font=35,
                    command=lambda btns_num = btns_num: button_press(btns_num+1)))
        btns[btns_num].grid(row=x, column=y)

button0 = Button(frame,text=0, height=4, width=9, font=35,
                    command=lambda: button_press(0))
button0.grid(row=3, column = 0)

plus = Button(frame,text='+', height=4, width=9, font=35,
                    command=lambda: button_press('+'))
plus.grid(row=0, column = 3)

minus = Button(frame,text='-', height=4, width=9, font=35,
                    command=lambda: button_press('-'))
minus.grid(row=1, column = 3)

mul = Button(frame,text='*', height=4, width=9, font=35,
                    command=lambda: button_press('*'))
mul.grid(row=2, column = 3)

div = Button(frame,text='/', height=4, width=9, font=35,
                    command=lambda: button_press('/'))
div.grid(row=3, column = 3)

equal = Button(frame,text='=', height=4, width=9, font=35,
                    command=equals)
equal.grid(row=3, column=2)

dec = Button(frame,text='.', height=4, width=9, font=35,
                    command=lambda: button_press('.'))
dec.grid(row=3, column = 1)

clear = Button(window,text='clear', height=4, width=12, font=35,
                    command=clear)
clear.pack()

window.mainloop()