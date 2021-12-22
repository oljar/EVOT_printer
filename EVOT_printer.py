from tkinter import *
from tkinter import ttk
import datetime
from data_source import *


class Application (Frame):
    def __init__(self,master):


        super(Application,self).__init__(master)




    #  heater

        self.settings()
        self.identity()
        self.heater_choice()
        self.cooler_choice()
        self.fan_choice()
        self.supply_filter_choice()
        self.exhaust_filter_choice()
        self.damper()
        self.heat_exchanger()
        self.additional_exuipment()
        self.s_and_p()





    def settings(self):

        self.settings_frame = ttk.LabelFrame(tab0)
        self.settings_frame.pack(anchor=W, padx=15)

        self.inspector_name_value = StringVar()
        self.lbl_inspector_name = ttk.Label(self.settings_frame, text="konrtoler KJ").grid(row=1, column=1, padx=10, pady=(10,3))
        self.inspector_name = ('a','b','c')
        self.combobox_suplly = ttk.Combobox(self.settings_frame, values=self.inspector_name, textvariable=self.inspector_name_value).grid(row=1, column=2,  padx=10, pady=(10,3))



        self.selected_ahu_value = selected_ahu_value



        self.lbl_type = ttk.Label(self.settings_frame, text="typ EVO-T").grid(row=5, column=1, padx=10, pady=3)
        self.entry_type = ttk.Entry(self.settings_frame, textvariable= self.selected_ahu_value)
        self.entry_type.insert(END,self.selected_ahu_value)
        self.entry_type.grid(row=5, column=2,padx=10,ipadx=10, pady=(10,3))

        self.data_value = StringVar()
        self.data_act = datetime.date.today()
        self.data=ttk.Label(self.settings_frame ,text = "data").grid(row =15,column = 1,padx=10,pady=(10,3))
        self.entry_data=ttk.Entry(self.settings_frame,textvariable = self.data_value)




        self.data_button=ttk.Button(self.settings_frame,text = "data").grid(row = 15, column = 20, padx=10 , pady=(10,3) )



        self.entry_data.grid(row =15 ,column = 2,padx=1,pady=(10,3), ipadx=10 )

    def identity(self):

        self.identity_frame = ttk.LabelFrame(tab1)
        self.identity_frame.pack(anchor=W, padx=15)

   #   serial
        self.entry_serial_value = StringVar()
        self.lbl_serial=ttk.Label(self.identity_frame ,text = "Nr seryjny").grid(row =1,column = 1,padx=10,pady=(10,3))
        self.entry_serial=ttk.Entry(self.identity_frame,textvariable = self.entry_serial_value).grid(row =1 ,column = 2,padx=1,pady=(10,3), ipadx=10 )

    # order
        self.entry_order_value = StringVar()
        self.lbl_order=ttk.Label(self.identity_frame,text = "Zlecenie").grid(row = 5,column = 1,padx=10,pady=3)
        self.entry_order=ttk.Entry(self.identity_frame, textvariable = self.entry_order_value).grid(row =5,column = 2,padx=1,pady=3,ipadx=10 )

    # project
        self.entry_project_value = StringVar()
        self.lbl_project=ttk.Label(self.identity_frame ,text = "Projekt").grid(row = 10,column = 1,padx=10,pady=3)
        self.entry_project=ttk.Entry(self.identity_frame, textvariable = self.entry_project_value).grid(row =10,column = 2,padx=1,pady=3, ipadx=10 )

   #  system
        self.entry_system_value = StringVar()
        self.lbl_system = ttk.Label(self.identity_frame, text="System").grid(row=15, column=1, padx=10, pady=3)
        self.entry_system = ttk.Entry(self.identity_frame, textvariable = self.entry_system_value).grid(row=15, column=2, padx=1, pady=3, ipadx=10)



   #   type

        self.lbl_type = ttk.Label(self.identity_frame, text="typ EVO-T").grid(row=20, column=1, padx=10, pady=3)

        self.entry_type = ttk.Entry(self.identity_frame, textvariable = self.selected_ahu_value )
        self.entry_type.config(state=DISABLED)
        self.entry_type.insert(END,self.selected_ahu_value)
        self.entry_type.grid(row=20, column=2, padx=10, pady=3,ipadx=10)



    # supply
        self.selected_supply_value_in = StringVar
        self.selected_supply_value = selected_supply_value
        self.lbl_supply = ttk.Label(self.identity_frame, text="nawiew - wykonanie").grid(row=25, column=1, padx=10, pady=3)
        self.entry_type_supply = ttk.Entry(self.identity_frame, textvariable=self.selected_supply_value_in)
        self.entry_type_supply.insert(END,self.selected_supply_value)
        self.entry_type_supply.grid(row=25, column=2,  pady=3, ipadx=10)





    # supply_execution
        self.selected_supply_execution_value = StringVar()
        self.version_supply_execution = ('L', 'R')
        self.combobox_suplly_execution = ttk.Combobox(self.identity_frame, values=self.version_supply_execution,width = 5 ).grid(row=25, column=10)


    #supply_flow

        self.selected_supply_flow_value = StringVar()
        self.lbl_supply_flow = ttk.Label(self.identity_frame, text="    N - wydatek powietrza [m3/h]").grid(row=30, column=1, padx=10, pady=3)
        self.entry_supply_flow = ttk.Entry(self.identity_frame, textvariable = self.selected_supply_flow_value ).grid(row=30, column=2, padx=1, pady=3, ipadx=10)


    # supply_pressure

        self.entry_supply_pressure_value = StringVar()
        self.lbl_supply_pressure = ttk.Label(self.identity_frame, text="   N - spręż dyspozycyjny [Pa]").grid(row=35, column=1, padx=10, pady=3)
        self.entry_supply_pressure = ttk.Entry(self.identity_frame, textvariable = self.entry_supply_pressure_value ).grid(row=35, column=2, padx=1, pady=3, ipadx=10)



    #exhaust
        self.selected_exhaust_value_in = StringVar()
        self.selected_exhaust_value = selected_exhaust_value
        self.lbl_exhaust = ttk.Label(self.identity_frame, text="wywiew - wykonanie").grid(row=40, column=1, padx=10, pady=3)
        self.entry_type_exhaust = ttk.Entry(self.identity_frame, textvariable= self.selected_exhaust_value_in)
        self.entry_type_exhaust.insert(END,self.selected_exhaust_value)
        self.entry_type_exhaust.grid(row=40, column=2 ,  pady=3, ipadx=10)





    # exhaust_execution
        self.selected_exhaust_execution_value = StringVar()
        self.version_exhaust_execution = ('L', 'R')
        self.combobox_exhaust_execution = ttk.Combobox(self.identity_frame, values=self.version_exhaust_execution, textvariable=self.selected_exhaust_execution_value, width = 5 ).grid(row=40, column=10)


    # exhaust_flow
        self.entry_exhaust_flow_value  = StringVar()
        self.lbl_exhaust_flow = ttk.Label(self.identity_frame, text="    W - wydatek powietrza [m3/h]").grid(row=45, column=1, padx=10, pady=3)
        self.entry_exhaust_flow = ttk.Entry(self.identity_frame, textvariable = self.entry_exhaust_flow_value ).grid(row=45, column=2, padx=1, pady=3, ipadx=10)


    # exhaust_pressure
        self.entry_exhaust_pressure_value = StringVar()
        self.lbl_exhaust_pressure = ttk.Label(self.identity_frame, text="   W - spręż dyspozycyjny [Pa]").grid(row=50, column=1, padx=10, pady=3)
        self.entry_exhaust_pressure = ttk.Entry(self.identity_frame, textvariable = self.entry_exhaust_pressure_value ).grid(row=50, column=2, padx=1, pady=3, ipadx=10)




    # mass
        self.mass_value = StringVar()
        self.mass=ttk.Label(self.identity_frame ,text = "masa urządzenia [kg]").grid(row = 55,column = 1,padx=10,pady=3)
        self.entry_mass=ttk.Entry(self.identity_frame,textvariable = self.mass_value)
        self.entry_mass.insert(END,mass_value)
        self.entry_mass.grid(row = 55 ,column = 2,padx=1,pady=3, ipadx=10 )


#heater
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
                self.lbl_symbol_electric_heater = ttk.Label(self.lframe, text="typ NE" ).grid(row=5, column=1,padx=1)
                self.entry_symbol_electric_heater = ttk.Entry(self.lframe, textvariable = self.symbol_electric_heater_value, width = 30)
                self.entry_symbol_electric_heater.insert(END,symbol_electric_heater_value )
                self.entry_symbol_electric_heater.grid(row=5, column=5, padx=2)



                # heater data  for plate
                self.electric_heater_plate_value = StringVar()
                self.lbl_plate_electric_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_electric_heater = ttk.Entry(self.lframe, textvariable = self.electric_heater_plate_value,width = 30)
                self.entry_plate_electric_heater.insert(END, electric_heater_plate_value_in)
                self.entry_plate_electric_heater.grid(row=10, column=5, padx=2, ipadx=4,pady=10 )



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
                self.lbl_symbol_water_heater = ttk.Label(self.lframe, text="typ WN" ).grid(row=5, column=1,padx = 3)
                self.entry_symbol_water_heater = ttk.Entry(self.lframe, textvariable = self.symbol_water_heater_value,width = 30 )
                self.entry_symbol_water_heater.insert(END, symbol_water_heater_value)
                self.entry_symbol_water_heater.grid(row=5, column=5, padx = 3)


                # water heater data  for plate
                self.water_heater_plate_value = StringVar()
                self.lbl_plate_water_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_water_heater = ttk.Entry(self.lframe, textvariable=self.water_heater_plate_value, width=30)
                self.entry_plate_water_heater.insert(END, water_heater_plate_value)
                self.entry_plate_water_heater.grid(row=10, column=5, padx=2, ipadx=4, pady=10)


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
                self.lbl_reverse_exchanger = ttk.Label(self.lframe, text=" typ RE").grid(row=5, column=1, padx =3)
                self.entry_reverse_exchanger = ttk.Entry(self.lframe, textvariable=self.symbol_reverse_exchanger_value,width = 30)
                self.entry_reverse_exchanger.insert(END, symbol_reverse_exchanger_value)
                self.entry_reverse_exchanger.grid(row=5, column=5,padx = 3)



                # reverse heater data  for plate
                self.reverse_heater_plate_value = StringVar()
                self.lbl_plate_reverse_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_reverse_heater = ttk.Entry(self.lframe, textvariable = self.reverse_heater_plate_value,width = 30)
                self.entry_plate_reverse_heater.insert(END, reverse_heater_plate_value)
                self.entry_plate_reverse_heater.grid(row=10, column=5, padx=2, ipadx=4,pady=10 )

                #explanation
                self.explanation = ttk.Label(self.lframe, text="moc lato [KW] / czynnik " ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )





    def lackoff_heater_function(self):

        try :
            self.lframe.destroy()
        except :
            pass





#cooler
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
            self.lbl_symbol_water_cooler= ttk.Label(self.lframe, text="typ CHW" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_water_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_water_cooler_value,width = 30 )
            self.entry_symbol_water_cooler.insert(END, symbol_water_cooler_value)
            self.entry_symbol_water_cooler.grid(row=5, column=5, padx = 3)


            # water cooler data  for plate
            self.water_cooler_plate_value = StringVar()
            self.lbl_plate_water_cooler = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1, padx=2, ipadx=4, pady=10)
            self.entry_plate_water_cooler = ttk.Entry(self.lframe, textvariable=self.water_cooler_plate_value, width=30)
            self.entry_plate_water_cooler.insert(END, water_cooler_plate_value)
            self.entry_plate_water_cooler.grid(row=10, column=5, padx=2, ipadx=4, pady=10)


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

            self.symbol_refrageration_cooler_value = StringVar()
            self.lbl_symbol_refrageration_cooler = ttk.Label(self.lframe, text="typ CHF" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_refrageration_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_refrageration_cooler_value,width = 30 )
            self.entry_symbol_refrageration_cooler.insert(END, symbol_refrageration_cooler_value)
            self.entry_symbol_refrageration_cooler.grid(row=5, column=5, padx = 3)



            # water cooler data  for plate
            self.refrageration_cooler_plate_value = StringVar()
            self.lbl_plate_refrageration_cooler = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_plate_refrageration_cooler = ttk.Entry(self.lframe, textvariable=self.refrageration_cooler_plate_value, width=30)
            self.entry_plate_refrageration_cooler.insert(END, refrageration_cooler_plate_value )
            self.entry_plate_refrageration_cooler.grid(row=10, column=5, padx=2, ipadx=4, pady=10)

            #explanation
            self.explanation = ttk.Label(self.lframe, text=" moc lato [kW]/ czynnik" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )


    def lackoff_cooler_function(self):
        try :
            self.lframe.destroy()
        except :
            pass


#Fans
#######################################################################################################################

    def fan_choice(self):
        self.lfradio = ttk.LabelFrame(tab4)
        self.lfradio.pack( )
        self.fan_choice_value = IntVar()
        self.EC_fan = ttk.Radiobutton(self.lfradio, text ="EC wentylator ", variable = self.fan_choice_value, value = 1, command = self.EC_fan_function).grid(row =0, column = 0, padx=20, pady = 5)
        self.AC_fan = ttk.Radiobutton(self.lfradio, text ="AC wentylator ", variable = self.fan_choice_value, value = 2, command = self.AC_fan_function).grid(row =0, column = 5, padx=20, pady = 5)
        self.lackoff_supply_fan = ttk.Radiobutton(self.lfradio, text="brak", variable = self.fan_choice_value, value= 4, command = self.lackoff_fan_function).grid (row = 0, column = 20, padx=20, pady = 5)


    def EC_fan_function(self):

        try :
            self.lframe.destroy()
        except:
            pass
        finally:

            #supply_fan symbol
            self.lframe = ttk.LabelFrame(tab4, text= "EC - wentylator")
            self.lframe.pack( anchor = W, padx=7 )

            self.symbol_EC_supply_fan_value = StringVar()
            self.lbl_symbol_EC_supply_fan= ttk.Label(self.lframe, text="nawiew-typ-EC" ).grid(row=5, column=1,padx = 3,pady = 10)
            self.entry_symbol_EC_supply_fan = ttk.Entry(self.lframe, textvariable = self.symbol_EC_supply_fan_value,width = 30 )
            self.entry_symbol_EC_supply_fan.insert(END, symbol_EC_supply_fan_value)
            self.entry_symbol_EC_supply_fan.grid(row=5, column=5, padx = 1)



            # Power - EC_supply_fan
            self.power_EC_supply_fan_value = StringVar()
            self.lbl_power_plate_EC_supply_fan = ttk.Label(self.lframe, text="moc [kW]" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_power_plate_EC_supply_fan = ttk.Entry(self.lframe, textvariable=self.power_EC_supply_fan_value , width=10)
            self.entry_power_plate_EC_supply_fan.insert(END, power_EC_supply_fan_value )
            self.entry_power_plate_EC_supply_fan.grid(row=10, column=5, padx=(0,100))

            # Voltage - EC_supply_fan

            self.voltage_EC_supply_fan_value = StringVar()
            self.lbl_voltage_plate_EC_supply_fan = ttk.Label(self.lframe, text="napięcie zasilania [V]" ).grid(row=15, column=1,padx=1,pady = 10)
            self.entry_voltage_plate_EC_supply_fan = ttk.Entry(self.lframe, textvariable=self.voltage_EC_supply_fan_value, width=10)
            self.entry_voltage_plate_EC_supply_fan.insert(END, voltage_EC_supply_fan_value)
            self.entry_voltage_plate_EC_supply_fan.grid(row=15, column=5, padx=(0,100))

            # frequency - EC_supply_fan

            self.frequency_EC_supply_fan_value = StringVar()
            self.lbl_frequency_plate_EC_supply_fan = ttk.Label(self.lframe, text="częstotliwość [Hz]").grid(row=20, column=1,padx=1, pady=10)
            self.entry_frequency_plate_EC_supply_fan = ttk.Entry(self.lframe, textvariable=self.frequency_EC_supply_fan_value, width=10)
            self.entry_frequency_plate_EC_supply_fan.insert(END, frequency_EC_supply_fan_value )
            self.entry_frequency_plate_EC_supply_fan.grid(row=20, column=5, padx=(0, 100))

            # quantity - EC_supply_fan

            self.quantity_EC_supply_fan_value = StringVar()
            self.lbl_quantity_EC_supply_fan = ttk.Label(self.lframe, text="ilość").grid(row=25, column=1, padx=1, pady=10)
            self.entry_quantity_plate_EC_supply_fan = ttk.Entry(self.lframe, textvariable=self.quantity_EC_supply_fan_value, width=10)
            self.entry_quantity_plate_EC_supply_fan.insert(END, quantity_EC_supply_fan_value)
            self.entry_quantity_plate_EC_supply_fan.grid(row=25, column=5, padx=(0, 100))

            # Symbol - EC_exhaust_fan

            self.symbol_EC_exhaust_fan_value = StringVar()
            self.lbl_symbol_EC_exhaust_fan= ttk.Label(self.lframe, text="wywiew-typ-EC" ).grid(row=5, column=10,padx = 3,pady = 10)
            self.entry_symbol_EC_exhaust_fan = ttk.Entry(self.lframe, textvariable = self.symbol_EC_exhaust_fan_value, width = 30 )
            self.entry_symbol_EC_exhaust_fan.insert(END, symbol_EC_exhaust_fan_value)
            self.entry_symbol_EC_exhaust_fan.grid(row=5, column=15, padx = 1)

            # Power - EC_exhaust_fan
            self.power_EC_exhaust_fan_value = StringVar()
            self.lbl_power_plate_EC_exhaust_fan = ttk.Label(self.lframe, text="moc [kW]" ).grid(row=10, column=10,padx=1,pady = 10)
            self.entry_power_plate_EC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.power_EC_exhaust_fan_value, width=10)
            self.entry_power_plate_EC_exhaust_fan.insert(END, power_EC_exhaust_fan_value)
            self.entry_power_plate_EC_exhaust_fan.grid(row=10, column=15, padx=(0,100))

            self.voltage_EC_exhaust_fan_value = StringVar()
            self.lbl_voltage_plate_EC_exhaust_fan = ttk.Label(self.lframe, text="napięcie zasilania [V]" ).grid(row=15, column=10,padx=1,pady = 10)
            self.entry_voltage_plate_EC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.voltage_EC_exhaust_fan_value, width=10)
            self.entry_voltage_plate_EC_exhaust_fan.insert(END, voltage_EC_exhaust_fan_value)
            self.entry_voltage_plate_EC_exhaust_fan.grid(row=15, column=15, padx=(0,100))

            self.frequency_EC_exhaust_fan_value = StringVar()
            self.lbl_frequency_plate_EC_exhaust_fan = ttk.Label(self.lframe, text="częstotliwość [Hz]").grid(row=20, column=10,padx=1, pady=10)
            self.entry_frequency_plate_EC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.frequency_EC_exhaust_fan_value, width=10)
            self.entry_frequency_plate_EC_exhaust_fan .insert(END, frequency_EC_exhaust_fan_value)
            self.entry_frequency_plate_EC_exhaust_fan .grid(row=20, column=15, padx=(0, 100))


            self.quantity_EC_exhaust_fan_value = StringVar()
            self.lbl_quantity_EC_exhaust_fan = ttk.Label(self.lframe, text="ilość").grid(row=25, column=10, padx=1, pady=10)
            self.entry_quantity_plate_EC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.quantity_EC_exhaust_fan_value, width=10)
            self.entry_quantity_plate_EC_exhaust_fan.insert(END, quantity_EC_exhaust_fan_value)
            self.entry_quantity_plate_EC_exhaust_fan.grid(row=25, column=15, padx=(0, 100))




    def AC_fan_function(self):

            try:
                self.lframe.destroy()
            except:
                pass
            finally:

                # AC supply
                self.lframe = ttk.LabelFrame(tab4, text = "AC - wentylator")
                self.lframe.pack(anchor=W)
                self.lframe.pack(anchor=W, padx=7)


                self.symbol_AC_supply_fan_value = StringVar()
                self.lbl_symbol_AC_supply_fan = ttk.Label(self.lframe, text="nawiew-typ-AC").grid(row=5, column=1, padx=3, pady=10)
                self.entry_symbol_AC_supply_fan = ttk.Entry(self.lframe, textvariable=self.symbol_AC_supply_fan_value, width=30)
                self.entry_symbol_AC_supply_fan.insert(END, symbol_AC_supply_fan_value)
                self.entry_symbol_AC_supply_fan.grid(row=5, column=5, padx=1)

                # Power - AC_supply_fan
                self.power_AC_supply_fan_value = StringVar()
                self.lbl_power_plate_AC_supply_fan = ttk.Label(self.lframe, text="moc [kW]").grid(row=10, column=1, padx=1, pady=10)
                self.entry_power_plate_AC_supply_fan = ttk.Entry(self.lframe, textvariable=self.power_AC_supply_fan_value, width=10)
                self.entry_power_plate_AC_supply_fan.insert(END, power_AC_supply_fan_value)
                self.entry_power_plate_AC_supply_fan.grid(row=10, column=5, padx=(0, 100))

                #Voltage - AC_supply_fan

                self.voltage_AC_supply_fan_value = StringVar()
                self.lbl_voltage_plate_AC_supply_fan = ttk.Label(self.lframe, text="napięcie zasilania [V]").grid(row=15, column=1, padx=1, pady=10)
                self.entry_voltage_plate_AC_supply_fan = ttk.Entry(self.lframe, textvariable=self.voltage_AC_supply_fan_value, width=10)
                self.entry_voltage_plate_AC_supply_fan.insert(END, voltage_AC_supply_fan_value)
                self.entry_voltage_plate_AC_supply_fan.grid(row=15, column=5, padx=(0, 100))

                # frequency- AC_supply_fan

                self.frequency_AC_supply_fan_value = StringVar()
                self.lbl_frequency_plate_AC_supply_fan = ttk.Label(self.lframe, text="częstotliwość [Hz]").grid(row=20, column=1, padx=1, pady=10)
                self.entry_frequency_plate_AC_supply_fan = ttk.Entry(self.lframe, textvariable=self.frequency_AC_supply_fan_value, width=10)
                self.entry_frequency_plate_AC_supply_fan.insert(END, frequency_AC_supply_fan_value)
                self.entry_frequency_plate_AC_supply_fan.grid(row=20, column=5, padx=(0, 100))

                # quantity- AC_supply_fan

                self.quantity_AC_supply_fan_value = StringVar()
                self.lbl_quantity_AC_supply_fan = ttk.Label(self.lframe, text="ilość").grid(row=25, column=1, padx=1, pady=10)
                self.entry_quantity_plate_AC_supply_fan = ttk.Entry(self.lframe, textvariable=self.quantity_AC_supply_fan_value, width=10)
                self.entry_quantity_plate_AC_supply_fan.insert(END, quantity_AC_supply_fan_value)
                self.entry_quantity_plate_AC_supply_fan.grid(row=25, column=5, padx=(0, 100))





                # AC exhaust
                self.symbol_AC_exhaust_fan_value = StringVar()
                self.lbl_symbol_AC_exhaust_fan = ttk.Label(self.lframe, text="wywiew-typ-AC").grid(row=5, column=10, padx=3, pady=10)
                self.entry_symbol_AC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.symbol_AC_exhaust_fan_value, width=30)
                self.entry_symbol_AC_exhaust_fan.insert(END, symbol_AC_exhaust_fan_value)
                self.entry_symbol_AC_exhaust_fan.grid(row=5, column=15, padx=1)

                # Power - AC_exhaust_fan
                self.power_AC_exhaust_fan_value = StringVar()
                self.lbl_power_plate_AC_exhaust_fan = ttk.Label(self.lframe, text="moc [kW]").grid(row=10, column=10, padx=1, pady=10)
                self.entry_power_plate_AC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.power_AC_exhaust_fan_value, width=10)
                self.entry_power_plate_AC_exhaust_fan.insert(END, power_AC_exhaust_fan_value)
                self.entry_power_plate_AC_exhaust_fan.grid(row=10, column=15, padx=(0, 100))

                self.voltage_AC_exhaust_fan_value = StringVar()
                self.lbl_voltage_plate_AC_exhaust_fan = ttk.Label(self.lframe, text="napięcie zasilania [V]").grid(row=15, column=10, padx=1, pady=10)
                self.entry_voltage_plate_AC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.voltage_AC_exhaust_fan_value, width=10)
                self.entry_voltage_plate_AC_exhaust_fan.insert(END, voltage_AC_exhaust_fan_value)
                self.entry_voltage_plate_AC_exhaust_fan.grid(row=15, column=15, padx=(0, 100))


                self.frequency_AC_exhaust_fan_value = StringVar()
                self.lbl_frequency_plate_AC_exhaust_fan = ttk.Label(self.lframe, text="częstotliwość [Hz]").grid(row=20, column=10, padx=1, pady=10)
                self.entry_frequency_plate_AC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.frequency_AC_exhaust_fan_value, width=10)
                self.entry_frequency_plate_AC_exhaust_fan.insert(END, frequency_AC_exhaust_fan_value)
                self.entry_frequency_plate_AC_exhaust_fan.grid(row=20, column=15, padx=(0, 100))


                self.quantity_AC_exhaust_fan_value = StringVar()
                self.lbl_quantity_AC_exhaust_fan = ttk.Label(self.lframe, text="ilość").grid(row=25, column=10, padx=1, pady=10)
                self.entry_quantity_plate_AC_exhaust_fan = ttk.Entry(self.lframe, textvariable=self.quantity_AC_exhaust_fan_value, width=10)
                self.entry_quantity_plate_AC_exhaust_fan.insert(END, quantity_AC_exhaust_fan_value)
                self.entry_quantity_plate_AC_exhaust_fan.grid(row=25, column=15, padx=(0, 100))








    def lackoff_fan_function(self) :
        try:
            self.lframe.destroy()
        except:
            pass

####################################################################################################################################





###################################################################################################################################


    def supply_filter_choice(self):
        self.lfradio = ttk.LabelFrame(tab5)
        self.lfradio.pack( )
        self.filter_choice_value = IntVar()
        self.G4_supply_filter = ttk.Radiobutton(self.lfradio, text = "G4", variable = self.filter_choice_value, value = 1, command = self.G4_supply_filter_function).grid(row =0, column = 0, padx=20, pady = 5)
        self.M5_supply_filter = ttk.Radiobutton(self.lfradio, text = "M5", variable = self.filter_choice_value, value = 2, command = self.M5_supply_filter_function).grid(row =0, column = 5, padx=20, pady = 5)
        self.F7_supply_filter = ttk.Radiobutton(self.lfradio, text = "F7", variable = self.filter_choice_value, value = 3, command = self.F7_supply_filter_function).grid(row =0, column = 10, padx=20, pady = 5)
        self.F9_supply_filter = ttk.Radiobutton(self.lfradio, text = "F9", variable = self.filter_choice_value, value = 4, command = self.F9_supply_filter_function).grid(row =0, column = 15, padx=20, pady = 5)
        self.lackoff_supply_fan = ttk.Radiobutton(self.lfradio, text="brak", variable = self.filter_choice_value, value= 5, command = self.lackoff_supply_filter_function).grid (row = 0, column = 20, padx=20, pady = 5)



    def G4_supply_filter_function(self):

        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter G4  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_G4_supply_filter_value = StringVar()
            self.lbl_symbol_G4_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_G4_supply_filter_value, width=30)
            self.entry_symbol_G4_supply_filter.insert(END, symbol_G4_supply_filter_value)
            self.entry_symbol_G4_supply_filter.grid(row=10, column=1, padx=1)


            #  supply filter G4 quantity
            self.quantity_G4_supply_filter_value = StringVar()
            self.lbl_quantity_G4_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_G4_supply_filter_value, width=10)
            self.entry_quantity_G4_supply_filter.insert(END, quantity_G4_supply_filter_value)
            self.entry_quantity_G4_supply_filter.grid(row=10, column=5, padx=1)




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

    def M5_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter M5  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_supply_filter_value = StringVar()
            self.lbl_symbol_M5_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_M5_supply_filter_value, width=30)
            self.entry_symbol_M5_supply_filter.insert(END, symbol_M5_supply_filter_value)
            self.entry_symbol_M5_supply_filter.grid(row=10, column=1, padx=1)



            #  supply filter M5 quantity
            self.quantity_M5_supply_filter_value = StringVar()
            self.lbl_quantity_M5_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_M5_supply_filter_value, width=10)
            self.entry_quantity_M5_supply_filter.insert(END, quantity_M5_supply_filter_value)
            self.entry_quantity_M5_supply_filter.grid(row=10, column=5, padx=1)


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

    def F7_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter F7  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F7_supply_filter_value = StringVar()
            self.lbl_symbol_F7_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F7_supply_filter_value, width=30)
            self.entry_symbol_F7_supply_filter.insert(END, symbol_F7_supply_filter_value)
            self.entry_symbol_F7_supply_filter.grid(row=10, column=1, padx=1)


            #  supply filter F7 quantity
            self.quantity_F7_supply_filter_value = StringVar()
            self.lbl_quantity_F7_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F7_supply_filter_value, width=10)
            self.entry_quantity_F7_supply_filter.insert(END, quantity_F7_supply_filter_value)
            self.entry_quantity_F7_supply_filter.grid(row=10, column=5, padx=1)




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)


    def F9_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter F9  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)

            self.symbol_F9_supply_filter_value = StringVar()
            self.lbl_symbol_F9_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F9_supply_filter_value, width=30)
            self.entry_symbol_F9_supply_filter.insert(END, symbol_F9_supply_filter_value )
            self.entry_symbol_F9_supply_filter.grid(row=10, column=1, padx=1)


            #  supply filter F9 quantity
            self.quantity_F9_supply_filter_value = StringVar()
            self.lbl_quantity_F9_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F9_supply_filter_value, width=10)
            self.entry_quantity_F9_supply_filter.insert(END, quantity_F9_supply_filter_value )
            self.entry_quantity_F9_supply_filter.grid(row=10, column=5, padx=1)


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

    def lackoff_supply_filter_function(self) :
        try:
            self.lframe.destroy()
        except:
            pass



##############################################################################################################################################


    def exhaust_filter_choice(self):
        self.lfradio = ttk.LabelFrame(tab6)
        self.lfradio.pack( )
        self.filter_choice_value = IntVar()
        self.G4_filter = ttk.Radiobutton(self.lfradio, text = "G4", variable = self.filter_choice_value, value = 1, command = self.G4_exhaust_filter_function).grid(row =0, column = 0, padx=20, pady = 5)
        self.M5_filter = ttk.Radiobutton(self.lfradio, text = "M5", variable = self.filter_choice_value, value = 2, command = self.M5_exhaust_filter_function).grid(row =0, column = 5, padx=20, pady = 5)
        self.F7_filter = ttk.Radiobutton(self.lfradio, text = "F7", variable = self.filter_choice_value, value = 3, command = self.F7_exhaust_filter_function).grid(row =0, column = 10, padx=20, pady = 5)
        self.F9_filter = ttk.Radiobutton(self.lfradio, text = "F9", variable = self.filter_choice_value, value = 4, command = self.F9_exhaust_filter_function).grid(row =0, column = 15, padx=20, pady = 5)
        self.lackoff_exhaust_fan = ttk.Radiobutton(self.lfradio, text="brak", variable = self.filter_choice_value, value= 5, command = self.lackoff_exhaust_filter_function).grid (row = 0, column = 20, padx=20, pady = 5)



    def G4_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter G4  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)

            self.symbol_G4_exhaust_filter_value = StringVar()
            self.lbl_symbol_G4_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_G4_exhaust_filter_value, width=30)
            self.entry_symbol_G4_exhaust_filter.insert(END, symbol_G4_exhaust_filter_value )
            self.entry_symbol_G4_exhaust_filter .grid(row=10, column=1, padx=1)




            #  exhaust filter G4 quantity
            self.quantity_G4_exhaust_filter_value = StringVar()
            self.lbl_quantity_G4_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_G4_exhaust_filter_value, width=10)
            self.entry_quantity_G4_exhaust_filter.insert(END, quantity_G4_exhaust_filter_value)
            self.entry_quantity_G4_exhaust_filter.grid(row=10, column=5, padx=1)




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)





    def M5_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter M5  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_exhaust_filter_value = StringVar()
            self.lbl_symbol_M5_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_M5_exhaust_filter_value, width=30)
            self.entry_symbol_M5_exhaust_filter.insert(END, symbol_M5_exhaust_filter_value )
            self.entry_symbol_M5_exhaust_filter.grid(row=10, column=1, padx=1)




            #  exhaust filter M5 quantity
            self.quantity_M5_exhaust_filter_value = StringVar()
            self.lbl_quantity_M5_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_M5_exhaust_filter_value, width=10)
            self.entry_quantity_M5_exhaust_filter.insert(END, quantity_M5_exhaust_filter_value )
            self.entry_quantity_M5_exhaust_filter.grid(row=10, column=5, padx=1)



            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)


    def F7_exhaust_filter_function(self):

        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter F7  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)

            self.symbol_F7_exhaust_filter_value = StringVar()
            self.lbl_symbol_F7_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F7_exhaust_filter_value, width=30)
            self.entry_symbol_F7_exhaust_filter.insert(END, symbol_F7_exhaust_filter_value )
            self.entry_symbol_F7_exhaust_filter.grid(row=10, column=1, padx=1)



            #  exhaust filter F7 quantity
            self.quantity_F7_exhaust_filter_value = StringVar()
            self.lbl_quantity_F7_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F7_exhaust_filter_value, width=10)
            self.entry_quantity_F7_exhaust_filter.insert(END, quantity_F7_exhaust_filter_value)
            self.entry_quantity_F7_exhaust_filter.grid(row=10, column=5, padx=1)


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

    def F9_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter F9  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)


            self.symbol_F9_exhaust_filter_value = StringVar()
            self.lbl_symbol_F9_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F9_exhaust_filter_value, width=30)
            self.entry_symbol_F9_exhaust_filter.insert(END, symbol_F9_exhaust_filter_value)
            self.entry_symbol_F9_exhaust_filter.grid(row=10, column=1, padx=1)



            #  exhaust filter F9 quantity
            self.quantity_F9_exhaust_filter_value = StringVar()
            self.lbl_quantity_F9_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F9_exhaust_filter_value, width=10)
            self.entry_quantity_F9_exhaust_filter.insert(END, quantity_F9_exhaust_filter_value)
            self.entry_quantity_F9_exhaust_filter.grid(row=10, column=5, padx=1)




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)




    def lackoff_exhaust_filter_function(self) :
        try:
            self.lframe.destroy()
        except:
            pass




    def damper(self):

        self.damper_frame = ttk.LabelFrame(tab7)

        self.damper_frame.pack(anchor=W, padx=15)
        self.symbol_supply_damper_value = StringVar()

        self.lbl_supply_symbol_damper = ttk.Label(self.damper_frame, text="tłumik nawiew - typ").grid(row=5, column=10, padx=3, pady=10)
        self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_supply_damper_value , width=30)

        self.entry_damper.insert(END, symbol_supply_damper_value)
        self.entry_damper.grid(row=5, column=15, padx=1)


        self.symbol_exaust_damper_value = StringVar()
        self.lbl_symbol_exhaust_damper = ttk.Label(self.damper_frame, text="tłumik wywiew - typ").grid(row=10, column=10, padx=3, pady=10)
        self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_exaust_damper_value , width=30)
        self.entry_damper.insert(END, symbol_exaust_damper_value)
        self.entry_damper.grid(row=10, column=15, padx=1)



    def heat_exchanger(self):

        self.heat_exchanger_frame = ttk.LabelFrame(tab8)
        self.heat_exchanger_frame.pack(anchor=W, padx=15)
        self.symbol_heat_exchanger_value = StringVar()
        self.lbl_symbol_heat_exchanger = ttk.Label(self.heat_exchanger_frame, text="wymiennik przeciwprądowy - typ").grid(row=5, column=10, padx=3, pady=10)
        self.entry_heat_exchanger = ttk.Entry(self.heat_exchanger_frame, textvariable=self.symbol_heat_exchanger_value , width=30)
        self.entry_heat_exchanger.insert(END, symbol_heat_exchanger_value )
        self.entry_heat_exchanger.grid(row=5, column=15, padx=1)





    def additional_exuipment(self):

        self.additional_exuipment_frame = ttk.LabelFrame(tab9)
        self.additional_exuipment_frame.pack(anchor=W, padx=15)

        self.lbl_additional_equipment= ttk.Label(self.additional_exuipment_frame, text="wyposażenie dodatkowe").grid(row=5, column=10, padx=3, pady=10)
        self.txt_additional_equipment = Text(self.additional_exuipment_frame , width=50, height = 20)
        self.txt_additional_equipment.insert("1.0", additional_exuipment_value)
        self.txt_additional_equipment.grid(row=5, column=15, padx=1)




    def s_and_p(self):

        self.s_and_p_frame = ttk.LabelFrame(tab10)
        self.s_and_p_frame.pack(anchor=W, padx=15)
        self.s_and_p_value =  StringVar()
        self.lbl_s_and_p= ttk.Label(self.s_and_p_frame, text="sprawdzenie i próby" ).grid(row=5, column=10, padx=3, pady=10)
        self.txt_s_and_p = Text(self.s_and_p_frame , width=50, height = 20)
        self.txt_s_and_p.insert("1.0", s_and_p_value)
        self.txt_s_and_p.grid(row=5, column=15, padx=1)









########################################################################################################################

window = Tk()
window.title("EVOT_printer")
window.geometry('650x400')

tab_parent = ttk.Notebook(window)

tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)
tab7 = ttk.Frame(tab_parent)
tab8 = ttk.Frame(tab_parent)
tab9 = ttk.Frame(tab_parent)
tab10 = ttk.Frame(tab_parent)


tab_parent.add(tab0,text = 'ustaw')
tab_parent.add(tab1,text = 'identyfikacja')
tab_parent.add(tab2,text = 'nagrzewnica')
tab_parent.add(tab3,text = 'chłodnica')
tab_parent.add(tab4,text = 'wentylatory')
tab_parent.add(tab5,text = 'flt-nawiew')
tab_parent.add(tab6,text = 'flt-wywiew')
tab_parent.add(tab7,text = 'tłumik')
tab_parent.add(tab8,text = 'odzysk')
tab_parent.add(tab9,text = 'wyp_dod')
tab_parent.add(tab10,text = 's&p')
tab_parent.pack(expand =1, fill = 'both')


app =Application(window)


#check
window.mainloop()


