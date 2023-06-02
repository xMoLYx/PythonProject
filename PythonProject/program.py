import sqlite3 as sl
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from PIL import ImageTk

#FUNCTIONS
def connection():
    con = sl.connect('studentdata.db')
    mycursor = con.cursor()
    query = 'create table if not exists students(studid varchar(200) primary key not null, fname varchar(100) not null, lname varchar(100) not null, address varchar(200) not null, phone varchar(50)not null)'
    mycursor.execute(query)
    return con

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.place(x= 280, y = 475)

def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    con = connection()
    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM students")
    results = mycursor.fetchall()
    con.commit()
    con.close()
    return results

def add():
    studid = str(idEntry.get())
    fname = str(firstnameEntry.get())
    lname = str(lastnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            con = connection()
            mycursor = con.cursor()
            mycursor.execute("INSERT INTO students VALUES ('"+studid+"','"+fname+"','"+lname+"','"+address+"','"+phone+"') ")
            con.commit()
            con.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            con = connection()
            mycursor = con.cursor()
            mycursor.execute("DELETE FROM students")
            con.commit()
            con.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            con = connection()
            mycursor = con.cursor()
            mycursor.execute("DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
            con.commit()
            con.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        studid = str(my_tree.item(selected_item)['values'][0])
        fname = str(my_tree.item(selected_item)['values'][1])
        lname = str(my_tree.item(selected_item)['values'][2])
        address = str(my_tree.item(selected_item)['values'][3])
        phone = str(my_tree.item(selected_item)['values'][4])

        setph(studid,1)
        setph(fname,2)
        setph(lname,3)
        setph(address,4)
        setph(phone,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    studid = str(idEntry.get())
    fname = str(firstnameEntry.get())
    lname = str(lastnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    con = connection()
    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM students WHERE STUDID='"+
    studid+"' or FNAME='"+
    fname+"' or LNAME='"+
    lname+"' or ADDRESS='"+
    address+"' or PHONE='"+
    phone+"' ")
    
    try:
        result = mycursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        con.commit()
        con.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedStudid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    studid = str(idEntry.get())
    fname = str(firstnameEntry.get())
    lname = str(lastnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            con = connection()
            mycursor = con.cursor()
            mycursor.execute("UPDATE students SET STUDID='"+
            studid+"', FNAME='"+
            fname+"', LNAME='"+
            lname+"', ADDRESS='"+
            address+"', PHONE='"+
            phone+"' WHERE STUDID='"+
            selectedStudid+"' ")
            con.commit()
            con.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()
#GUI

program = Tk()
program.title('Student Registration System')
background = ImageTk.PhotoImage(file = 'SRS.png')

bgLabel = Label(program, image = background)
program.geometry('1366x768')
bgLabel.grid()
my_tree = ttk.Treeview(program)

ph1 = tkinter.StringVar()
ph2 = tkinter.StringVar()
ph3 = tkinter.StringVar()
ph4 = tkinter.StringVar()
ph5 = tkinter.StringVar()

idLabel = Label(program, text = 'Studdent ID', font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
firstnameLabel = Label(program, text = 'Firstname', font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
lastnameLabel = Label(program, text = 'Lastname', font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
addressLabel = Label(program, text = 'Address', font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
phoneLabel = Label(program, text = 'Phone', font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')

idLabel.place(x = 200, y = 200)
firstnameLabel.place(x = 222, y = 250)
lastnameLabel.place(x = 226, y = 300)
addressLabel.place(x = 246, y = 350)
phoneLabel.place(x = 270, y = 400)

idEntry = Entry(program, width = 25, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
firstnameEntry = Entry(program, width = 25, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
lastnameEntry = Entry(program, width = 25, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
addressEntry = Entry(program, width = 25, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')
phoneEntry = Entry(program, width = 25, font = ('Codec Pro Extra Bold', 20, 'bold'), bd = 0, fg = 'black')

idEntry.place(x = 375, y = 200)
firstnameEntry.place(x = 375, y = 250)
lastnameEntry.place(x = 375, y = 300)
addressEntry.place(x = 375, y = 350)
phoneEntry.place(x = 375, y = 400)

addButton = Button(program, text = 'Add', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = add)
updateButton = Button(program, text = 'Update', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = update)
deleteButton = Button(program, text = 'Delete', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = delete)
seachButton = Button(program, text = 'Search', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = search)
resetButton = Button(program, text = 'Reset', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = reset)
selectButton = Button(program, text = 'Select', font = ('Codec Pro Extra Bold', 20, 'bold underline'), bg = 'white', fg = 'black', cursor = 'hand2', activebackground = 'white', activeforeground = 'white', width = 10, bd = 5, pady = 7, command = select)

addButton.place(x= 757, y = 200)
updateButton.place(x= 757, y = 280)
deleteButton.place(x= 757, y = 360)
seachButton.place(x= 950, y = 200)
resetButton.place(x= 950, y = 280)
selectButton.place(x= 950, y = 360)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Stud ID","Firstname","Lastname","Address","Phone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stud ID", anchor=W, width=170)
my_tree.column("Firstname", anchor=W, width=150)
my_tree.column("Lastname", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Stud ID", text="Student ID", anchor=W)
my_tree.heading("Firstname", text="Firstname", anchor=W)
my_tree.heading("Lastname", text="Lastname", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)

refreshTable()

program.mainloop()