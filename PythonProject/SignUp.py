from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#FUNCTIONS
def emailEnter(event):
    if emailEntry.get() == 'email':
        emailEntry.delete(0, END)

def userEnter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def passwordEnter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def repPassEnter(event): 
    if repPassEntry.get() == 'Confirm Password':
        repPassEntry.delete(0, END)

def hide():
    view.config(file = 'hide.png')
    passwordEntry.config(show = '*')
    repPassEntry.config(show = '*')
    eyeButton.config(command = show)

def show():
    view.config(file = 'view.png')
    passwordEntry.config(show = '')
    repPassEntry.config(show = '')
    eyeButton.config(command = hide)

def login_page():
    signup_window.destroy()
    import LogIn

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    repPassEntry.delete(0,END)

def connect_DataBase():
    if emailEntry.get() == 'email' or emailEntry.get() == '' or usernameEntry.get() == 'Username' or usernameEntry.get() == '' or passwordEntry.get() == 'Password' or passwordEntry.get() == '' or repPassEntry.get() == 'Confirm Password' or repPassEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != repPassEntry.get():
        messagebox.showerror('Error', 'Passwords do not match')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = '')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issue, please try again')
            return

        
        
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username = %s'
        mycursor.execute(query, (usernameEntry.get()))
        rowUsername = mycursor.fetchone()
        query = 'select * from data where email = %s'
        mycursor.execute(query, (emailEntry.get()))
        rowEmail = mycursor.fetchone()
        if rowUsername != None:
            messagebox.showerror('Error', 'Username already exists!')
        elif rowEmail != None:
            messagebox.showerror('Error', 'Email is already associated with another acoount!')
        else:
            query = 'insert into data(email, username, password) values(%s, %s, %s)'
            mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registartion is succesful!')
            clear()
            signup_window.destroy()
            import LogIn



#GUI
signup_window = Tk()
signup_window.title('Sign Up')
background = ImageTk.PhotoImage(file = 'SignUp.png')

bgLabel = Label(signup_window, image = background)
signup_window.geometry('1366x768')
signup_window.resizable(0,0)
bgLabel.grid()

emailEntry = Entry(signup_window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
emailEntry.place(x = 337, y = 215)
emailEntry.insert(0,'email')
emailEntry.bind('<FocusIn>', emailEnter)

usernameEntry = Entry(signup_window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
usernameEntry.place(x = 770, y = 215)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', userEnter)

passwordEntry = Entry(signup_window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
passwordEntry.place(x = 337, y = 353)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', passwordEnter)

repPassEntry = Entry(signup_window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
repPassEntry.place(x = 770, y = 353)
repPassEntry.insert(0,'Confirm Password')
repPassEntry.bind('<FocusIn>', repPassEnter)

signupButton = Button(signup_window, text = 'Sign Up', font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black', height = 2, width = 11, command = connect_DataBase)
signupButton.place(x = 587, y = 530)

view = PhotoImage(file = 'view.png')
eyeButton = Button(signup_window, image = view, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place(x = 337, y = 450)

showPass = Label(signup_window, text = 'Show Password', font = ('Codec Pro Extra Bold', 12, 'bold'), fg = 'black', height = 1, width = 13)
showPass.place(x = 361, y = 451)

check = IntVar()
termsandconditions = Checkbutton(text = 'I agree to Terms & Conditions', font = ('Codec Pro Extra Bold', 12, 'bold'), fg = 'black', height = 1, cursor = 'hand2', variable = check)
termsandconditions.place(x = 560, y = 495)

alreadyAccount = Label(signup_window, text = 'Already have an account?', font = ('Codec Pro Extra Bold', 12, 'bold'), bg = 'white', fg = 'black', height = 1)
alreadyAccount.place(x = 558, y = 623)

loginButton = Button(signup_window, text = 'Log In', font = ('Codec Pro Extra Bold', 12, 'bold underline'), bg = 'white', fg = 'blue', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', height = 1, command = login_page)
loginButton.place(x= 757, y = 620)

signup_window.mainloop()
