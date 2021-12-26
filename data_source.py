import fillpdf
from fillpdf import fillpdfs
import re
from tkinter import filedialog
import os
from tkinter import *
from tkinter import ttk









def open_pattern_File():

    global path
    path = filedialog.askdirectory()



def get_data ():

    path_plate = os.path.join(path,'tabliczka.pdf')
    path_cert = os.path.join(path,'atest.pdf')

    data_plate = fillpdfs.get_form_fields(path_plate)
    data_cert = fillpdfs.get_form_fields(path_cert)

    selected_ahu_value = "EVO-T"

    #

    pos = re.search("R|L$", (data_plate['supply']))

    selected_supply_value = (data_plate['supply'])[:(pos.span())[0]]

    ahu_range = re.findall(r'\d+',selected_supply_value)[0] # wielkość centrali



    selected_exhaust_value = (data_plate['exhaust'])[:(pos.span())[0]]





    symbol_electric_heater_value = data_cert['Pole tekstowe 8']
    electric_heater_plate_value_in = data_plate['electric heater s']
    mass_value= data_plate['weight t'] + ' ' + data_plate['weight u']
    version_type=('jhj','kjkjhk','ccccc')
    symbol_water_heater_value = data_cert['Pole tekstowe 8']
   # water_heater_plate_value = data_plate['heatre I s']

    get_data.water_heater_plate_value='działa'
    symbol_reverse_exchanger_value = "symbol_reverse_exchanger_value"
    reverse_heater_plate_value = "reverse_heater_plate_value"
    symbol_water_cooler_value = data_cert['Pole tekstowe 7']
    water_cooler_plate_value = data_plate['cooler s']


    symbol_refrageration_cooler_value = data_cert['Pole tekstowe 7']
    refrageration_cooler_plate_value = data_plate['cooler s']

    symbol_EC_supply_fan_value = data_cert['Pole tekstowe 27'].split()[0]
    power_EC_supply_fan_value  = data_cert['Pole tekstowe 9'].split()[0]
    voltage_EC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    frequency_EC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    quantity_EC_supply_fan_value = 1
    symbol_EC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split()[1]
    power_EC_exhaust_fan_value =  data_cert['Pole tekstowe 9'].split()[1]
    voltage_EC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    frequency_EC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    quantity_EC_exhaust_fan_value = 1
    power_AC_supply_fan_value = data_cert['Pole tekstowe 27'].split()[0]
    symbol_AC_supply_fan_value = data_cert['Pole tekstowe 9'].split()[0]
    voltage_AC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    frequency_AC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    quantity_AC_supply_fan_value = 1
    symbol_AC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split()[1]
    power_AC_exhaust_fan_value = data_cert['Pole tekstowe 9'].split()[1]
    voltage_AC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    frequency_AC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    quantity_AC_exhaust_fan_value = 1


    symbol_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_F9_exhaust_filter_value  = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_F9_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]

    symbol_supply_damper_value = f'Sekcja tłmik szumu- nawiew {ahu_range}'
    symbol_exaust_damper_value = f'Sekcja tłmik szumu- wywiew {ahu_range}'
    symbol_heat_exchanger_value =f'wym. przeciwprądowy  EVOT {ahu_range} CPR H'
    additional_exuipment_value = "additional_exuipment_value_1"
    s_and_p_value = "s_and_p_value_1"
    print ('dane pobrane')
    return get_data



try :

    get_data ()


except:

    data_plate = fillpdfs.get_form_fields('tabliczka.pdf')
    data_cert = fillpdfs.get_form_fields('atest.pdf')
    get_data.water_heater_plate_value = "odśwież"
    print(data_plate)
    print('######')
    print(data_cert)


    selected_ahu_value = "EVO-T"

    #




    pos = re.search("R|L$", (data_plate['supply']))




    selected_supply_value = (data_plate['supply'])[:(pos.span())[0]]

    ahu_range = re.findall(r'\d+',selected_supply_value)[0] # wielkość centrali



    selected_exhaust_value = (data_plate['exhaust'])[:(pos.span())[0]]





    symbol_electric_heater_value = data_cert['Pole tekstowe 8']
    electric_heater_plate_value_in = data_plate['electric heater s']
    mass_value= data_plate['weight t'] + ' ' + data_plate['weight u']
    version_type=('jhj','kjkjhk','ccccc')
    symbol_water_heater_value = data_cert['Pole tekstowe 8']
    water_heater_plate_value = data_plate['heatre I s']
    symbol_reverse_exchanger_value = "symbol_reverse_exchanger_value"
    reverse_heater_plate_value = "reverse_heater_plate_value"
    symbol_water_cooler_value = data_cert['Pole tekstowe 7']
    water_cooler_plate_value = data_plate['cooler s']


    symbol_refrageration_cooler_value = data_cert['Pole tekstowe 7']
    refrageration_cooler_plate_value = data_plate['cooler s']

    symbol_EC_supply_fan_value = data_cert['Pole tekstowe 27'].split()[0]
    power_EC_supply_fan_value  = data_cert['Pole tekstowe 9'].split()[0]
    voltage_EC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    frequency_EC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    quantity_EC_supply_fan_value = 1
    symbol_EC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split()[1]
    power_EC_exhaust_fan_value =  data_cert['Pole tekstowe 9'].split()[1]
    voltage_EC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    frequency_EC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    quantity_EC_exhaust_fan_value = 1
    power_AC_supply_fan_value = data_cert['Pole tekstowe 27'].split()[0]
    symbol_AC_supply_fan_value = data_cert['Pole tekstowe 9'].split()[0]
    voltage_AC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    frequency_AC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    quantity_AC_supply_fan_value = 1
    symbol_AC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split()[1]
    power_AC_exhaust_fan_value = data_cert['Pole tekstowe 9'].split()[1]
    voltage_AC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    frequency_AC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    quantity_AC_exhaust_fan_value = 1


    symbol_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    quantity_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    symbol_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    symbol_F9_exhaust_filter_value  = data_cert['Pole tekstowe 25'].split('/')[1]
    quantity_F9_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]



    symbol_supply_damper_value = f'Sekcja tłmik szumu- nawiew {ahu_range}'
    symbol_exaust_damper_value = f'Sekcja tłmik szumu- wywiew {ahu_range}'
    symbol_heat_exchanger_value =f'wym. przeciwprądowy  EVOT {ahu_range} CPR H'
    additional_exuipment_value = "additional_exuipment_value_1"
    s_and_p_value = "s_and_p_value_1"



