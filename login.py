import mysql.connector 
from tkinter import *
from tkinter import messagebox
import server
from mysql.connector import Error


conn = server.conn
window = Tk()
window.title("Login")

height = 650
width = 550

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = (screen_width / 3) - (width / 3)
y = (screen_height /2) - (height / 2)
window.geometry(f"{height}x{width}+{int(x)}+{int(y)}")
window.configure(bg="#333333")


# Python Scripts

def Login(event=NONE): # Login Function
    uname = username.get()
    pword = password.get()

    
    
    try:
        if conn.is_connected():
            pst = conn.cursor()
            query = "SELECT * FROM accounts WHERE username = %s AND password = %s"
            pst.execute(query, (uname, pword))   
            user_data = pst.fetchone()  
                
            

            if not all([uname,pword]):
                messagebox.showerror(title="Message", message = "Invalid Username or Password!")
                return
            elif user_data is None:
                messagebox.showerror(title="Message", message = "Incorrect Username or Password!")
                username.delete(0, END)
                password.delete(0, END)
                return
    
            else:
                accrole = user_data[1] # Accessing the index of accroles in the database 'desktopdb'


                if accrole == 'Admin':
                    messagebox.showinfo(title="Message", message = "Login Successfully!")
                    window.destroy()
                    import admindashboard

                    
                else:
                    messagebox.showinfo(title="Message", message = "Login Successfully!")
                    window.destroy()
                    import dashboard


    except Error as e:
        messagebox.showerror(title="Message", message="Connection Failed!")
        
window.bind("<Return>", Login)

def Register():
    window.destroy()
    import register

# Creating Widgets

Title = Label(window, text = "Login", font= ("Arial Bold", 30), bg = "#333333")
unamelabel = Label(window, text ="Username: ", font =("Arial",16), bg ="#333333")
username = Entry(window, text="Username", font=("Arial, 16"))
username.insert(0, "Enter your Username")
username.configure(state=DISABLED)
passlabel = Label(window, text="Password: ", font =("Arial",16), bg ="#333333")
password = Entry(window, text ="Password", font =("Arial",16))
password.insert(0, "Enter your Password")
password.configure(state=DISABLED)
forgotpass = Label(window, text = "Forgot Password?", font = ("Arial", 14), bg = "#333333")
loginbtn = Button(window, text = "Login", font =("Arial", 16), bg="green", fg="black", command = Login) 
registerbtn = Button(window, text = "Register", font =("Arial", 16), bg="blue", fg="black", command= Register)


# Event Part

def on_click(event):
    username.configure(state=NORMAL)
    username.delete(0, END)

    username.unbind("<Button-1>", on_click_id)
    
on_click_id = username.bind("<Button-1>", on_click)


def on_click(event):
    password.configure(state=NORMAL, show="•")
    password.delete(0, END)

    password.unbind("<Button-1>", on_click_2)

on_click_2 = password.bind("<Button-1>", on_click)





# Placing Widgets on the screen

Title.place(x = 275, y = 60)
unamelabel.place(x=120, y = 160)
username.place(x=123, y= 190, height = 30, width=400)
passlabel.place(x=120, y=230)
password.place(x=123, y= 260, height = 30, width=400)
forgotpass.place(x=365, y=290)
#loginbtn.place(x=123, y= 330, width=400)
loginbtn.place(x=120, y=330, width= 190)
registerbtn.place(x=333, y=330, width= 190)

window.mainloop()