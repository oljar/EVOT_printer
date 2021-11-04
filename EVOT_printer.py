from tkinter import *
from tkinter import ttk



class Application (Frame):
    def __init__(self,master):

       super(Application,self).__init__(master)
       self.serial()
       self.order()
       self.project()

    def serial(self):
        self.lbl_serial=Label(window ,text = "Nr seryjny").grid(row =1,column = 1,padx=10,pady=(10,3))
        self.entry_serial=Entry(window).grid(row =1 ,column = 2,padx=1,pady=(10,3) )

    def order(self):
        self.lbl_order=Label(window ,text = "Zlecenie").grid(row = 5,column = 1,padx=10,pady=3)
        self.lbl_order=Entry(window).grid(row =5,column = 2,padx=1,pady=3 )

    def project(self):
        self.lbl_order=Label(window ,text = "Project").grid(row = 10,column = 1,padx=10,pady=3)
        self.lbl_order=Entry(window).grid(row =10,column = 2,padx=1,pady=3 )




        # selected_month = StringVar()
        #
        # months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        #           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        #
        # month_cb = ttk.Combobox(window , values = months ,textvariable=selected_month ).grid(row=40,column = 4)
        #
        # print(selected_month.get())
        #
        #
        # def self.clicked():
        #      print(selected_month.get())


window = Tk()
window.title("EVOT_printer")
window.geometry('400x400')



app =Application(window)
window.mainloop()