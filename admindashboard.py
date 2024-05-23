import mysql.connector
from tkinter import *
from tkinter import messagebox 
import server


window = Tk()
window.title("Admin Dashboard")
height = 650
width = 550

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

window.mainloop()