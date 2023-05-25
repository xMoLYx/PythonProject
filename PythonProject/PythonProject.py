from distutils.filelist import translate_pattern
from tkinter import *
from tkinter import ttk
from turtle import heading, width
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

#FUNCTIONS

def userEnter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def passwordEnter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

#GUI
loginScreen = Tk()
loginScreen.geometry('1366x768')
loginScreen.resizable(0,0)
loginScreen.title('Python Project')
loginScreen.wm_attributes('-transparent', '#ab23ff')


##
style = ThemedStyle(loginScreen)
style.configure('Transparent.TEntry', fieldbackground='rgba(255, 255, 255, 0.3)')
##

bgImage = ImageTk.PhotoImage(file='LogIn.png')

bgLabel = Label(loginScreen, image = bgImage)
bgLabel.grid(row = 0, column = 0)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

usernameEntry = ttk.Entry(loginScreen, style = 'Transparent.TEntry',width = 18, font = ('Codec Pro Extra Bold', 20, 'bold'))
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

hide = PhotoImage(file = 'hide.png')
eyeButton = Button(loginScreen, image = hide, bd = 0)
eyeButton.place(x = 1100, y = 399)

loginScreen.mainloop()
