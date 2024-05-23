import mysql.connector
import server
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Dashboard")
height = 650
width = 850

screen_width = window.winfo_screenwidth() 
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y= (screen_height / 2) - (height / 2)

window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
window.configure(bg = "#333333")

window.mainloop()
