from tkinter import *
from turtle import heading, width
from PIL import ImageTk

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

passwordEntry = Entry(loginScreen, width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
passwordEntry.place(x = 860, y = 395)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', passwordEnter)

frame2 = Frame(loginScreen, width = 272, height = 2, bg = '#101728')
frame2.place(x = 860, y = 430)

view = PhotoImage(file = 'view.png')
eyeButton = Button(loginScreen, image = view, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place(x = 1100, y = 399)

forgetButton = Button(loginScreen, text = 'Forgot your password?', bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', font = ('Codec Pro Extra Bold', 9))
forgetButton.place(x = 999, y = 433)

loginButton = Button(loginScreen, text = "Login", font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black')
loginButton.place(x = 946, y = 529)

signupButton = Button(loginScreen, text = 'Sign Up', font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black', height = 2, width = 11, command = goSignUp)
signupButton.place(x = 127, y = 434)

loginScreen.mainloop()
