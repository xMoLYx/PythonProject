from email import message
from tkinter import *
from tkinter import messagebox
from tkinter.tix import WINDOW
from turtle import heading, width
from PIL import ImageTk
import pymysql

#FUNCTIONS

def userEnter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def passwordEnter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def hide():
    view.config(file = 'hide.png')
    passwordEntry.config(show = '*')
    eyeButton.config(command = show)

def show():
    view.config(file = 'view.png')
    passwordEntry.config(show = '')
    eyeButton.config(command = hide)

def goSignUp():
    loginScreen.destroy() 
    import SignUp

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required!')

    else:
        try:
            con = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = '')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issue, please try again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row ==  None:
            messagebox.showerror('Error', 'Invalid username or password!')
        else:
            messagebox.showinfo('Welcome', 'Success!')

def forget():
    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file = 'reset.png')
    bgLabel = Label(window, image = bgPic)
    bgLabel.grid()

    def userEnter(event):
        if usernameField.get() == 'Username':
            usernameField.delete(0, END)

    def passwordEnter(event):
        if passwordField.get() == 'Password':
            passwordField.delete(0, END)

    def repPassEnter(event): 
        if confirmPassword.get() == 'Confirm Password':
            confirmPassword.delete(0, END)

    usernameField = Entry(window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, bg = '#ab23ff', fg = 'black')
    usernameField.place(x = 200, y = 170)
    usernameField.insert(0, 'Username')
    usernameField.bind('<FocusIn>', userEnter)

    passwordField = Entry(window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, bg = '#ab23ff', fg = 'black')
    passwordField.place(x = 200, y = 250)
    passwordField.insert(0,'Password')
    passwordField.bind('<FocusIn>', passwordEnter)

    confirmPassword = Entry(window, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
    confirmPassword.place(x = 200, y = 330)
    confirmPassword.insert(0,'Confirm Password')
    confirmPassword.bind('<FocusIn>', repPassEnter)

    changeButton = Button(window, text = "Change Password", font = ('Codec Pro Extra Bold', 13, 'bold'), fg = 'black')
    changeButton.place(x = 257, y = 340)


    window.mainloop()


#GUI
loginScreen = Tk()
loginScreen.geometry('1366x768')
loginScreen.resizable(0,0)
loginScreen.title('Python Project')

bgImage = ImageTk.PhotoImage(file='LogIn.png')

bgLabel = Label(loginScreen, image = bgImage)
bgLabel.grid(row = 0, column = 0)

usernameEntry = Entry(loginScreen, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, bg = '#ab23ff', fg = 'black')
usernameEntry.place(x = 860, y = 260)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', userEnter)


frame1 = Frame(loginScreen, width = 272, height = 2, bg = '#101728')
frame1.place(x = 860, y = 295)

passwordEntry = Entry(loginScreen, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black', bg = 'purple')
passwordEntry.place(x = 860, y = 395)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', passwordEnter)

frame2 = Frame(loginScreen, width = 272, height = 2, bg = '#101728')
frame2.place(x = 860, y = 430)

view = PhotoImage(file = 'view.png')
eyeButton = Button(loginScreen, image = view, bd = 0, bg = 'purple', activebackground = 'purple', cursor = 'hand2', command = hide)
eyeButton.place(x = 1100, y = 399)

forgetButton = Button(loginScreen, text = 'Forgot your password?', bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', font = ('Codec Pro Extra Bold', 9), command = forget)
forgetButton.place(x = 999, y = 433)

loginButton = Button(loginScreen, text = "Login", font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black', command = login_user)
loginButton.place(x = 946, y = 529)

signupButton = Button(loginScreen, text = 'Sign Up', font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black', height = 2, width = 11, command = goSignUp)
signupButton.place(x = 127, y = 434)

loginScreen.mainloop()
