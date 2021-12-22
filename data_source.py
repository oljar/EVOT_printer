import fillpdf
from fillpdf import fillpdfs
import re

data_plate = fillpdfs.get_form_fields('tabliczka.pdf')
data_cert = fillpdfs.get_form_fields('atest.pdf')
# data_dict = {'supply': 'EVO-T COMPACT 4100 R', 'evo': 'EVO-T', 'exhaust': 'EVO-T COMPACT 4100 R', 'year prod': '2021', 'serial no': '210262174608000001', 'prod order no': '9035012', 'air flow s': '1150', 'fan set s': None, 'fan set e': None, 'air flow e': '620', 'external press s': '200', 'fan el mot s': 'EVOT 4100 VF1 EC ', 'fan el mot e': 'EVOT 4100 VF1 EC ', 'external press e': '200', 'comp un s': '0.5/ 230', 'comp un e': '0.5/ 230', 'heatre I e': None, 'heatre II s': None, 'pre filt 1 s': None, 'pre filt 1 e': None, 'heatre II e': None, 'electric heater s': '7.4/ [5.40/ 3 x 400]', 'pre filt 2 s': 'F7/ 592x287x75 / 1', 'pre filt 2 e': 'blelel 1', 'sec filt 2 s': None, 'sec filt 2 e': None, 'electric heater e': None, 'pre filt 3 e': None, 'sec filt 3 s': None, 'sec filt 3 e': None, 'cooler e': '', 'Humidifier s': None, 'sec filt 1 s': None, 'sec filt 1 e': None, 'sec filt 4 s': None, 'sec filt 4 e': None, 'Humidifier e': None, 'pump el motor t': None, 'heat recovery t': 'Wymiennik przeciwprądowy\rEVOT 4100 CPR H', 'weight t': '182', 'project no': 'K-2021-08-043183,      1N1W', 'air flow': 'Wydatek powietrza', 'fan set': 'Silnik rotora/p-py gl.', 'external press': 'Ciśnienie dyspozycyjne', 'fan el mot': 'Wentylator', 'heatre I': 'Nagrzewnica I wodna', 'comp un': 'Silnik wentylatora', 'heatre II': 'Nagrzewnica II', 'pre filt 1': 'Agr. chłodniczy', 'electric heater': 'Nagrzewnica elektryczna', 'pre filt 2': 'Filtr wstępny', 'sec filt 2': 'Filtr II stopnia', 'cooler': 'Chłodnica', 'pre filt 3': 'Filtr wstępny', 'sec filt 3': 'Filtr III stopnia', 'Humidifier': 'Nawilżacz', 'sec filt 1': 'Filtr II stopnia', 'sec filt 4': 'Filtr III stopnia', 'pump el motor': 'Silnik p-py nawilż.', 'heat recovery': 'Odzysk ciepła', 'weight': 'Masa', 'air flow u': 'm³/h', 'fan set u': 'kW/V', 'external press u': 'Pa', 'fan el mot u': 'typ', 'heatre I u': '°C/kW/kPa ', 'comp un u': 'kW/V', 'heatre II u': '°C/kW/kPa ', 'pre filt 1 u': ' V/Arozr/Amax', 'electric heater u': ' kW/[kW/V] ', 'pre filt 2 u': 'typ/rozm/szt.', 'sec filt 2 u': 'typ/rozm/szt.', 'cooler u': '°C/kW/kPa ', 'pre filt 3 u': 'typ/rozm/szt.', 'sec filt 3 u': 'typ/rozm/szt.', 'Humidifier u': '[kg/h]/kW/V', 'sec filt 1 u': 'typ/rozm/szt.', 'sec filt 4 u': 'typ/rozm/szt.', 'pump el motor u': 'kW/V/A', 'heat recovery u': 'typ', 'weight u': 'kg', 'cooler e 1': ''}
# fillpdfs.write_fillable_pdf('blank.pdf', 'new.pdf', data_dict)
print(data_plate)
print(data_cert)


selected_ahu_value = "EVO-T"


pos = re.search("R|L$", (data_plate['supply']))

selected_supply_value = (data_plate['supply'])[:(pos.span())[0]]

selected_exhaust_value = (data_plate['exhaust'])[:(pos.span())[0]]


print (pos.span())



symbol_electric_heater_value = data_cert['Pole tekstowe 8']
electric_heater_plate_value_in = data_plate['electric heater s']
mass_value= data_plate['weight t'] + ' ' + data_plate['weight u']
version_type=('jhj','kjkjhk','ccccc')
symbol_water_heater_value = data_cert['Pole tekstowe 8']
water_heater_plate_value = data_plate['heatre I s']
symbol_reverse_exchanger_value = "symbol_reverse_exchanger_value"
reverse_heater_plate_value = "reverse_heater_plate_value"
symbol_water_cooler_value = data_cert['Pole tekstowe 7']
water_cooler_plate_value = "water_cooler_plate_value"
symbol_refrageration_cooler_value ="symbol_refrageration_cooler_value"
refrageration_cooler_plate_value = "refrageration_cooler_plate_value "
symbol_EC_supply_fan_value = "symbol_EC_supply_fan_value"
power_EC_supply_fan_value  = "power_EC_supply_fan_value "
voltage_EC_supply_fan_value = "voltage_EC_supply_fan_value,"
frequency_EC_supply_fan_value = "frequency_EC_supply_fan_value"
quantity_EC_supply_fan_value = "quantity_EC_supply_fan_value"
symbol_EC_exhaust_fan_value = "symbol_EC_exhaust_fan_value"
power_EC_exhaust_fan_value = "power_EC_exhaust_fan_value"
voltage_EC_exhaust_fan_value = "voltage_EC_exhaust_fan_value"
frequency_EC_exhaust_fan_value = "frequency_EC_exhaust_fan_value"
quantity_EC_exhaust_fan_value = "quantity_EC_exhaust_fan_value"
power_AC_supply_fan_value = "power_AC_supply_fan_value"
symbol_AC_supply_fan_value = "symbol_AC_supply_fan_value"
voltage_AC_supply_fan_value = "voltage_AC_supply_fan_value"
frequency_AC_supply_fan_value = "frequency_AC_supply_fan_value"
quantity_AC_supply_fan_value = "quantity_AC_supply_fan_value"
symbol_AC_exhaust_fan_value = "symbol_AC_exhaust_fan_value"
power_AC_exhaust_fan_value = "power_AC_exhaust_fan_value"
voltage_AC_exhaust_fan_value = "voltage_AC_exhaust_fan_value"
frequency_AC_exhaust_fan_value = "frequency_AC_exhaust_fan_value"
quantity_AC_exhaust_fan_value = "quantity_AC_exhaust_fan_value"
symbol_G4_supply_filter_value = "symbol_G4_supply_filter_value"
quantity_G4_supply_filter_value = "quantity_G4_supply_filter_value"
symbol_M5_supply_filter_value = "symbol_M5_supply_filter_value"
quantity_M5_supply_filter_value = "quantity_M5_supply_filter_value"
symbol_F7_supply_filter_value = "symbol_F7_supply_filter_value"
quantity_F7_supply_filter_value = "quantity_F7_supply_filter_value"
symbol_F9_supply_filter_value = "symbol_F9_supply_filter_value"
quantity_F9_supply_filter_value = "quantity_F9_supply_filter_value"
symbol_G4_exhaust_filter_value = "symbol_G4_exhaust_filter_value"
quantity_G4_exhaust_filter_value = "quantity_G4_exhaust_filter_value)"
symbol_M5_exhaust_filter_value = "symbol_M5_exhaust_filter_value"
quantity_M5_exhaust_filter_value = "quantity_M5_exhaust_filter_value"
symbol_F7_exhaust_filter_value = "symbol_F7_exhaust_filter_value "
quantity_F7_exhaust_filter_value ="quantity_F7_exhaust_filter_value"
symbol_F9_exhaust_filter_value  = "symbol_F9_exhaust_filter_value"
quantity_F9_exhaust_filter_value = "quantity_F9_exhaust_filter_value"
symbol_supply_damper_value = "symbol_supply_damper_value"
symbol_exaust_damper_value = "symbol_exaust_damper_value"
symbol_heat_exchanger_value = "symbol_heat_exchanger_value"
additional_exuipment_value = "additional_exuipment_value_1"
s_and_p_value = "s_and_p_value_1"