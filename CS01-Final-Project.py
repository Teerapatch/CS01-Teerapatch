from tkinter import*
from types import LambdaType

root = Tk()
root.title("CALCULATOR")
operator = " "
text_Input = StringVar()

def btpress(numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btClear() :
    global operator
    operator = " "
    text_Input.set(" ")

def btnEqual() :
    global operator
    result= str(eval(operator))
    text_Input.set(result)

textDisplay = Entry(font = ('arial', 25, 'bold') ,textvariable = text_Input ,bd=25 ,bg = "pink" ,justify = "right").grid(columnspan = 4)

bt1 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "1" , command = lambda:btpress(1)).grid(row = 1 ,column = 0)
bt2 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "2" , command = lambda:btpress(2)).grid(row = 1 ,column = 1)
bt3 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "3" , command = lambda:btpress(3)).grid(row = 1 ,column = 2)
btdivide = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "/" , command = lambda:btpress("/")).grid(row = 1 ,column = 3)
bt4 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "4" , command = lambda:btpress(4)).grid(row = 2 ,column = 0)
bt5 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "5" , command = lambda:btpress(5)).grid(row = 2 ,column = 1)
bt6 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "6" , command = lambda:btpress(6)).grid(row = 2 ,column = 2)
btsum = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "*" , command = lambda:btpress("*")).grid(row = 2 ,column = 3)
bt7 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "7" , command = lambda:btpress(7)).grid(row = 3 ,column = 0)
bt8 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "8" , command = lambda:btpress(8)).grid(row = 3 ,column = 1)
bt9 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "9" , command = lambda:btpress(9)).grid(row = 3 ,column = 2)
btplus = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "+" , command = lambda:btpress("+")).grid(row = 3 ,column = 3)
btClear = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "C" , command = btClear).grid(row = 4 ,column = 0)
bt0 = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "0" , command = lambda:btpress(0)).grid(row = 4 ,column = 1)
btequal = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "=" , command = btnEqual).grid(row = 4 ,column = 2)
btminus = Button(padx = 15 ,bd = 6 ,font = ('arial', 25, 'bold') , text = "-" , command = lambda:btpress("-")).grid(row = 4 ,column = 3)

root.mainloop()