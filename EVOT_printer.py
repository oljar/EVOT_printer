from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
a1 = ttk.Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)

selected_month = StringVar()

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

month_cb = ttk.Combobox(window , values = months ,textvariable=selected_month ).grid(row=4,column = 4)

print(selected_month.get())


def clicked():
    print(selected_month.get())


btn = Button(window ,text="Submit",command= clicked).grid(row=4,column=0)


window.mainloop()