from tkinter import *
from tkinter import ttk
import time


class Application (Frame):
    def __init__(self,master):

       super(Application,self).__init__(master)

    #  idetyty
       self.serial()
       self.order()
       self.project()
       self.system()
       self.type()
       self.supply()
       self.supply_execution()
       self.supply_flow()
       self.supply_pressure()
       self.exhaust()
       self.exhaust_execution()
       self.exhaust_flow()
       self.exhaust_pressure()

    #  heater


       self.heater_choice()
       self.cooler_choice()






    def serial(self):
        self.entry_serial_value = StringVar()
        self.lbl_serial=ttk.Label(tab1 ,text = "Nr seryjny").grid(row =1,column = 1,padx=10,pady=(10,3))
        self.entry_serial=ttk.Entry(tab1,textvariable = self.entry_serial_value).grid(row =1 ,column = 2,padx=1,pady=(10,3), ipadx=10 )

    def order(self):
        self.entry_order_value = StringVar()
        self.lbl_order=ttk.Label(tab1,text = "Zlecenie").grid(row = 5,column = 1,padx=10,pady=3)
        self.entry_order=ttk.Entry(tab1, textvariable = self.entry_order_value).grid(row =5,column = 2,padx=1,pady=3,ipadx=10 )

    def project(self):
        self.entry_project_value = StringVar()
        self.lbl_project=ttk.Label(tab1 ,text = "Projekt").grid(row = 10,column = 1,padx=10,pady=3)
        self.entry_project=ttk.Entry(tab1, textvariable = self.entry_project_value).grid(row =10,column = 2,padx=1,pady=3, ipadx=10 )

    def system(self):
        self.entry_system_value = StringVar()
        self.lbl_system = ttk.Label(tab1, text="System").grid(row=15, column=1, padx=10, pady=3)
        self.entry_system = ttk.Entry(tab1, textvariable = self.entry_system_value).grid(row=15, column=2, padx=1, pady=3, ipadx=10)



    def type(self):
            self.selected_type_value = StringVar()
            self.lbl_type = ttk.Label(tab1, text="Typ").grid(row=20, column=1, padx=10, pady=3)
            self.version_type = ('a','b','c')
            self.combobox_type = ttk.Combobox(tab1, values=self.version_type, textvariable=self.selected_type_value).grid(row=20, column=2)


    def supply(self):

            self.selected_supply_value = StringVar()
            self.lbl_supply = ttk.Label(tab1, text="Nawiew - wykonanie").grid(row=25, column=1, padx=10, pady=3)
            self.version_supply = ('a','b','c')
            self.combobox_suplly = ttk.Combobox(tab1, values=self.version_supply, textvariable=self.selected_supply_value).grid(row=25, column=2)


    def supply_execution(self):
            self.selected_supply_execution_value = StringVar()
            self.version_supply_execution = ('a', 'b', 'c')
            self.combobox_suplly_execution = ttk.Combobox(tab1, values=self.version_supply_execution, textvariable=self.selected_supply_execution_value,width = 5 ).grid(row=25, column=10)


    def supply_flow(self):

           self.selected_supply_flow_value = StringVar()
           self.lbl_supply_flow = ttk.Label(tab1, text="    N - wydatek powietrza [m3/h]").grid(row=30, column=1, padx=10, pady=3)
           self.entry_supply_flow = ttk.Entry(tab1, textvariable = self.selected_supply_flow_value ).grid(row=30, column=2, padx=1, pady=3, ipadx=10)


    def supply_pressure(self):

            self.entry_supply_pressure_value = StringVar()
            self.lbl_supply_pressure = ttk.Label(tab1, text="   N - spręż dyspozycyjny [Pa]").grid(row=35, column=1, padx=10, pady=3)
            self.entry_supply_pressure = ttk.Entry(tab1, textvariable = self.entry_supply_pressure_value ).grid(row=35, column=2, padx=1, pady=3, ipadx=10)



    def exhaust(self):
            self.selected_exhaust_value = StringVar()
            self.lbl_exhaust = ttk.Label(tab1, text="Wywiew - wykonanie").grid(row=40, column=1, padx=10, pady=3)
            self.version_exhaust = ('a', 'b', 'c')
            self.combobox_exhaust = ttk.Combobox(tab1, values=self.version_exhaust, textvariable=self.selected_exhaust_value).grid(row=40, column=2)



    def exhaust_execution(self):
            self.selected_exhaust_execution_value = StringVar()
            self.version_exhaust_execution = ('a', 'b', 'c')
            self.combobox_exhaust_execution = ttk.Combobox(tab1, values=self.version_exhaust_execution, textvariable=self.selected_exhaust_execution_value, width = 5 ).grid(row=40, column=10)


    def exhaust_flow(self):
            self.entry_exhaust_flow_value  = StringVar()
            self.lbl_exhaust_flow = ttk.Label(tab1, text="    W - wydatek powietrza [m3/h]").grid(row=45, column=1, padx=10, pady=3)
            self.entry_exhaust_flow = ttk.Entry(tab1, textvariable = self.entry_exhaust_flow_value ).grid(row=45, column=2, padx=1, pady=3, ipadx=10)


    def exhaust_pressure(self):
            self.entry_exhaust_pressure_value = StringVar()
            self.lbl_exhaust_pressure = ttk.Label(tab1, text="   W - spręż dyspozycyjny [Pa]").grid(row=50, column=1, padx=10, pady=3)
            self.entry_exhaust_pressure = ttk.Entry(tab1, textvariable = self.entry_exhaust_pressure_value ).grid(row=50, column=2, padx=1, pady=3, ipadx=10)


#heater

    #Heater choice
    ############################################################################################################################


    def heater_choice(self):
            self.lfradio = ttk.LabelFrame(tab2)
            self.lfradio.pack( )
            self.heater_choice_value = IntVar()
            self.electric_heater = ttk.Radiobutton(self.lfradio,text = "nagrzewnica elektryczna", variable = self.heater_choice_value, value = 1,command = self.electric_heater_function ).grid(row =0,column = 0,padx=20, pady = 5 )
            self.water_heater = ttk.Radiobutton(self.lfradio,text = "nagrzewnica wodna", variable = self.heater_choice_value, value = 2, command = self.water_heater_function ).grid(row =0,column = 5,padx=20,pady = 5)
            self.reverse_exchanger = ttk.Radiobutton(self.lfradio, text="wymiennik rewersyjny", variable = self.heater_choice_value, value= 3,command = self.reverse_exchanger_function ).grid(row = 0,column = 15 ,padx=20,pady = 5)
            self. lackoff_heater = ttk.Radiobutton(self.lfradio, text="brak", variable = self.heater_choice_value , value= 4, command = self.lackoff_heater_function ).grid (row = 0,column = 20,padx=20, pady = 5)



    def electric_heater_function(self):

            try :

                self.lframe.destroy()
            except:
                pass

            finally:



                self.lframe = ttk.LabelFrame(tab2)
                self.lframe.pack( anchor = W, padx=7)

                #symbol electric heater
                self.symbol_electric_heater_value = StringVar()
                self.lbl_symbol_electric_heater = ttk.Label(self.lframe, text="symbol NE" ).grid(row=5, column=1,padx=1)
                self.entry_symbol_electric_heater = ttk.Entry(self.lframe, textvariable = self.symbol_electric_heater_value, width = 30).grid(row=5, column=5, padx=2)

                # heater data  for plate
                self.electric_heater_plate_value = StringVar()
                self.lbl_plate_electric_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_electric_heater = ttk.Entry(self.lframe, textvariable = self.electric_heater_plate_value,width = 30).grid(row=10, column=5, padx=2, ipadx=4,pady=10 )
                #
                #explanation
                self.explanation = ttk.Label(self.lframe, text="moc zima [kW] / ilość sekcji x moc sekcji [i x kW]/ napięcie zasialania [V] " ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )



    def water_heater_function(self):

            try :
                self.lframe.destroy()
            except:
                pass
            finally:

                #water heater symbol
                self.lframe = ttk.LabelFrame(tab2)

                self.lframe.pack( anchor = W)

                self.lframe.pack( anchor = W, padx=7)

                self.symbol_water_heater_value = StringVar()
                self.lbl_symbol_water_heater = ttk.Label(self.lframe, text="symbol WE" ).grid(row=5, column=1,padx = 3)
                self.entry_symbol_water_heater = ttk.Entry(self.lframe, textvariable = self.symbol_water_heater_value,width = 30 ).grid(row=5, column=5, padx = 3)



                # water heater data  for plate
                self.water_heater_plate_value = StringVar()
                self.lbl_plate_water_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_water_heater = ttk.Entry(self.lframe, textvariable=self.water_heater_plate_value, width=30).grid(row=10, column=5, padx=2, ipadx=4, pady=10)

                #explanation
                self.explanation = ttk.Label(self.lframe, text="zasilanie-powrót [stC] / moc zima [kW]/ spadek ciśnienia [kPa]" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )





    def reverse_exchanger_function(self):

            try :
                self.lframe.destroy()
            except:
                pass
            finally:
                self.lframe = ttk.LabelFrame(tab2)

                self.lframe.pack( anchor = W)

                self.lframe.pack( anchor = W, padx=7)

                self.symbol_reverse_exchanger_value = StringVar()
                self.lbl_reverse_exchanger = ttk.Label(self.lframe, text=" symbol RE").grid(row=5, column=1, padx =3)
                self.entry_reverse_exchanger= ttk.Entry(self.lframe, textvariable=self.symbol_reverse_exchanger_value,width = 30).grid(row=5, column=5,padx = 3)

                # reverse heater data  for plate
                self.reverse_heater_plate_value = StringVar()
                self.lbl_plate_reverse_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_reverse_heater = ttk.Entry(self.lframe, textvariable = self.reverse_heater_plate_value,width = 30).grid(row=10, column=5, padx=2, ipadx=4,pady=10 )

                #explanation
                self.explanation = ttk.Label(self.lframe, text="moc lato [KW] / czynnik " ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )




    def lackoff_heater_function(self):

        try :
            self.lframe.destroy()
        except :
            pass








        #
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
        # def self.clicked()
        #      print(selected_month.get())
#######################################################################################################################

    def cooler_choice(self):
        self.lfradio = ttk.LabelFrame(tab3)
        self.lfradio.pack( )
        self.cooler_choice_value = IntVar()
        self.water_cooler = ttk.Radiobutton(self.lfradio,text = "chłodnica wodna ", variable = self.cooler_choice_value, value = 1,command = self.water_cooler_function).grid(row =0,column = 0,padx=20, pady = 5 )
        self.refrageration_cooler = ttk.Radiobutton(self.lfradio,text = "chłodnica freonowa", variable = self.cooler_choice_value, value = 2, command = self.refrageration_cooler_function ).grid(row =0,column = 5,padx=20,pady = 5)
        self. lackoff_cooler = ttk.Radiobutton(self.lfradio, text="brak", variable = self.cooler_choice_value , value= 4, command = self.lackoff_cooler_function ).grid (row = 0,column = 20,padx=20, pady = 5)







    def water_cooler_function(self):

        try :
            self.lframe.destroy()
        except:
            pass
        finally:

            #water cooler symbol
            self.lframe = ttk.LabelFrame(tab3)

            self.lframe.pack( anchor = W)

            self.lframe.pack( anchor = W, padx=7)

            self.symbol_water_cooler_value = StringVar()
            self.lbl_symbol_water_cooler= ttk.Label(self.lframe, text="chłodnica wodna" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_water_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_water_cooler_value,width = 30 ).grid(row=5, column=5, padx = 3)



            # water cooler data  for plate
            self.water_cooler_plate_value = StringVar()
            self.lbl_plate_water_cooler= ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_plate_water_cooler = ttk.Entry(self.lframe, textvariable=self.water_cooler_plate_value, width=30).grid(row=10, column=5, padx=2, ipadx=4, pady=10)

            #explanation
            self.explanation = ttk.Label(self.lframe, text="[zasilanie - powrót [stC] / moc lato [kW]/ spadek ciśnienia [kPa]" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )





    def refrageration_cooler_function(self):

        try :
            self.lframe.destroy()
        except:
            pass
        finally:

            #water cooler symbol
            self.lframe = ttk.LabelFrame(tab3)

            self.lframe.pack( anchor = W)

            self.lframe.pack( anchor = W, padx=7)

            self.symbol_water_cooler_value = StringVar()
            self.lbl_symbol_water_cooler = ttk.Label(self.lframe, text="symbol WE" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_water_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_water_cooler_value,width = 30 ).grid(row=5, column=5, padx = 3)



            # water cooler data  for plate
            self.water_cooler_plate_value = StringVar()
            self.lbl_plate_water_cooler = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_plate_water_cooler = ttk.Entry(self.lframe, textvariable=self.water_cooler_plate_value, width=30).grid(row=10, column=5, padx=2, ipadx=4, pady=10)

            #explanation
            self.explanation = ttk.Label(self.lframe, text=" moc lato [kW]/ czynnik" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )


    def lackoff_cooler_function(self):
        try :
            self.lframe.destroy()
        except :
            pass



















window = Tk()
window.title("EVOT_printer")
window.geometry('650x400')

tab_parent = ttk.Notebook(window)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)
tab7 = ttk.Frame(tab_parent)
print('jjj')



tab_parent.add(tab1,text = 'identyfikacja')
tab_parent.add(tab2,text = 'nagrzewnica')
tab_parent.add(tab3,text = 'chłodnica')
tab_parent.add(tab4,text = 'wentylatory')
tab_parent.add(tab5,text = 'filtry')
tab_parent.add(tab6,text = 'tłumiki')
tab_parent.add(tab7,text = 'wymiennik')

tab_parent.pack(expand =1, fill = 'both')


app =Application(window)



window.mainloop()

