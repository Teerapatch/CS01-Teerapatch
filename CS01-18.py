from tkinter import *
root = Tk()
root.title("First GUI")
root.geometry("300x300")

Wata = Label(text = "My Name is" ,fg = "blue" ,font = 20).grid(row = 0 ,column = 0)
Chi = Label(text = "Teerapatch" ,fg = "orange" ,font = 20).grid(row = 1 ,column = 1)
wa = Label(text = "Baisod" ,fg = "pink" ,font = 20).grid(row = 2 ,column = 2)

root.mainloop()