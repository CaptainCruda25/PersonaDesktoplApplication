import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox
import server

conn = server.conn
window = Tk()
height = 650
width = 690

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2)-(width / 2)
y = (screen_height / 4) - (height / 4)

window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

window.title("Register")
window.configure(bg = "#333333")
window.resizable(False, False)



# Python Code Part

def Register(event=None):
    fname = firstname.get()
    lname = lastname.get()
    uname = username.get()
    pword = password.get()
    rpass = rpassword.get()

    
        
    

    try:
        if conn.is_connected():
            pst = conn.cursor()
            cursor = conn.cursor()
            search = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(search, (uname,))
            rs = cursor.fetchone()

            if rs:
                messagebox.showerror("Error", "Account Exist!")
                firstname.delete(0, END)
                lastname.delete(0, END)
                username.delete(0, END)
                password.delete(0, END)
                rpassword.delete(0, END)

            elif not all([fname, lname, uname, pword, rpass]):
                messagebox.showerror("Error", "Please Fill All The Fields!")
                return
            
            elif pword != rpass:
                messagebox.showerror("Error", "Password Doesn\'t Match!")
                return
            else:
                query = "INSERT INTO accounts(fname, lname, username, password) VALUES(%s, %s, %s, %s)"
                pst.execute(query, (fname, lname, uname, pword))
                conn.commit()
                messagebox.showinfo("Message","Register Successfully!")
                window.destroy()
                import login

        


    except Error as e:
        messagebox.showerror("Error", "Connection Failed!")


window.bind("<Return>", Register)

def Cancel(event=None):
    ask = messagebox.askquestion("Confirmation", "Are you want to cancel?")
    if ask == 'yes':
        window.destroy()
        import login
    else:
        return 




# Creating Widgets

title = Label(window, text ="Register", font = ("Arial Bold", 30), bg = "#333333")
fnamelabel = Label(window, text = "First Name:", font = ("Arial",16), bg ="#333333")
firstname = Entry(window, font=("Arial", 16))
firstname.insert(0, "Enter your First Name")
firstname.configure(state=DISABLED)
lnamelabel = Label(window, text = "Last Name: ", font =("Arial", 16), bg ="#333333")
lastname =Entry(window, font=("Arial", 16))
lastname.insert(0, "Enter your Last Name")
lastname.configure(state=DISABLED)
unamelabel = Label(window, text="Username: ", font=("Arial",16), bg ="#333333")
username = Entry(window, font = ("Arial", 16))
username.insert(0, "Enter a Username")
username.configure(state=DISABLED)
passlabel = Label(window, text ="Password: ", font= ("Arial", 16), bg ="#333333")
password = Entry(window, font=("Arial", 16))
password.insert(0, " Enter your Password")
password.configure(state=DISABLED)
rpasslabel = Label(window, text ="Repeat Password: ", font= ("Arial", 16), bg ="#333333")
rpassword = Entry(window, font=("Arial", 16))
rpassword.insert(0, " Repeat your Password")
rpassword.configure(state=DISABLED)
registerbtn = Button(window, text="✔ Ok", font=("Arial", 16), bg="green", fg="black", command = Register)
cancelbtn = Button(window, text = " ❌ Cancel", font=("Arial", 16), bg ="orange red", fg="black", command = Cancel )



# Event Part

def on_click(event):
    firstname.configure(state=NORMAL)
    firstname.delete(0,END)

    firstname.unbind("<Button-1>",on_click_id)
on_click_id = firstname.bind("<Button-1>", on_click)

def onclick(event):
    lastname.configure(state=NORMAL)
    lastname.delete(0, END)

    # Callback Methods
    lastname.unbind("<Button-1>", on_click_lname)

on_click_lname = lastname.bind("<Button-1>", onclick)

def uname(event):
    username.configure(state=NORMAL)
    username.delete(0, END)

    username.unbind("<Button-1>", onclick_uname)

onclick_uname = username.bind("<Button-1>", uname)

def passbtn(event):
    password.configure(state=NORMAL, show = "•")
    password.delete(0, END)

    password.unbind("<Button-1>", onclick_pass)

onclick_pass = password.bind("<Button-1>", passbtn)

def rpass(event):
    rpassword.configure(state = NORMAL, show = "•")
    rpassword.delete(0, END)

    rpassword.unbind("<Button-1>", onclick_rpass)

onclick_rpass = rpassword.bind("<Button-1>", rpass)

# Placing Widgets on the screen
title.place(x = 255, y = 60)
fnamelabel.place(x=123, y= 160)
firstname.place(x = 126, y = 190, width=400)
lnamelabel.place(x= 123, y= 230)
lastname.place(x= 126, y =260, width=400)
unamelabel.place(x=123, y = 300)
username.place(x=126, y= 330, width= 400)
passlabel.place(x=123, y = 370)
password.place(x=126, y=400, width=400)
rpasslabel.place(x=123, y=440)
rpassword.place(x=126, y=470, width=400)
registerbtn.place(x=126, y=530, width= 175)
cancelbtn.place(x = 350, y = 530, width = 175)

window.mainloop()

