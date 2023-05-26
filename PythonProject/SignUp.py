from tkinter import *
from PIL import ImageTk

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
    if repPassEntry.get() == 'Repeat Password':
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
repPassEntry.insert(0,'Repeat Password')
repPassEntry.bind('<FocusIn>', repPassEnter)

signupButton = Button(signup_window, text = 'Sign Up', font = ('Codec Pro Extra Bold', 20, 'bold'), fg = 'black', height = 2, width = 11)
signupButton.place(x = 587, y = 530)

view = PhotoImage(file = 'view.png')
eyeButton = Button(signup_window, image = view, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place(x = 337, y = 450)

showPass = Label(signup_window, text = 'Show Password', font = ('Codec Pro Extra Bold', 12, 'bold'), fg = 'black', height = 1, width = 13)
showPass.place(x = 361, y = 451)

termsandconditions = Checkbutton(text = 'I agree to Terms & Conditions', font = ('Codec Pro Extra Bold', 12, 'bold'), fg = 'black', height = 1)
termsandconditions.place(x = 560, y = 495)

alreadyAccount = Label(signup_window, text = 'Already have an account?', font = ('Codec Pro Extra Bold', 12, 'bold'), bg = 'white', fg = 'black', height = 1)
alreadyAccount.place(x = 650, y = 530)

signup_window.mainloop()
