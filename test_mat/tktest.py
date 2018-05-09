from tkinter import *

master = Tk()

w = Message(master, text="this is a message")
w.config(bd=2, relief=SUNKEN)
w.pack()

mainloop()()