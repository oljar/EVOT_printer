import sqlite3

conn = sqlite3.connect('baza.db')

c = conn.cursor()

query = """
CREATE TABLE "items" (
   

        
       
     
        -- settings
            "inspector_name_value"              TEXT,
            "mass_value"                        INTEGER,
            "data_value"                        TEXT,
        
        -- identity
            "entry_serial_value"                TEXT,
            "entry_order_value"                 TEXT,     
            "entry_project_value"               TEXT,
            "entry_system_value"                TEXT,
            "selected_type_value"               TEXT,
            "selected_supply_value"             TEXT,
            "selected_supply_execution_value"   TEXT, 
            "selected_supply_flow_value"        INTEGER, 
            "entry_supply_pressure_value"       INTEGER,
            "selected_exhaust_value"            TEXT,
            "selected_exhaust_execution_value"  TEXT, 
            "entry_exhaust_flow_value"          INTEGER,
            "entry_exhaust_pressure_value"      INTEGER,
            
        
        --electric heater
        
            "symbol_electric_heater_value"      TEXT,
            "electric_heater_plate_value"       TEXT,
        
        --electric heater
        
            "symbol_water_heater_value"         TEXT, 
            "water_heater_plate_value"          TEXT,
        
        --reverse exchanger   
           
            "symbol_reverse_exchanger_value"    TEXT,
            "everse_heater_plate_value"         TEXT, 
            
        --water cooler    
            "symbol_water_cooler_value"         TEXT, 
            "water_cooler_plate_value"          TEXT,       
        
        --refrgeration cooler        
            "symbol_refrageration_cooler_value"       TEXT,              
            "refrageration_cooler_plate_value "          TEXT,
            
        --supply EC fan   
            "symbol_EC_supply_fan_value"        TEXT, 
            "power_EC_supply_fan_value"         REAL,
            "voltage_EC_supply_fan_value"       INTEGER,   
            "frequency_EC_supply_fan_value"     REAL,  
            "quantity_EC_supply_fan_value"      INTEGER,
            
        --exhaust EC fan    
            
            "symbol_EC_exhaust_fan_value"       TEXT,
            "power_EC_exhaust_fan_value"        REAL, 
            "voltage_EC_exhaust_fan_value"      INTEGER, 
            "frequency_EC_exhaust_fan_value"    REAL, 
            "quantity_EC_exhaust_fan_value"     INTEGER,
        
        --supply AC fan 
        
            "symbol_AC_supply_fan_value"        TEXT, 
            "power_AC_supply_fan_value"         REAL, 
            "voltage_AC_supply_fan_value"       INTEGER,
            "frequency_AC_supply_fan_value"     REAL,     
            "quantity_AC_supply_fan_value"      INTEGER,
            
        --exhaust EC fan   
            "symbol_AC_exhaust_fan_value"       TEXT, 
            "power_AC_exhaust_fan_value"        REAL,
            "voltage_AC_exhaust_fan_value"      INTEGER,
            "frequency_AC_exhaust_fan_value"    REAL,
            "quantity_AC_exhaust_fan_value"     INTEGER,
            
        --filter supply   
        
        
            "symbol_G4_supply_filter_value"    TEXT,
            "quantity_G4_supply_filter_value"  TEXT,
            "symbol_M5_supply_filter_value"    TEXT,
            "quantity_M5_supply_filter_value"  TEXT,
            "symbol_F7_supply_filter_value"    TEXT,
            "quantity_F7_supply_filter_value"  TEXT,
            "symbol_F9_supply_filter_value"    TEXT,
            "quantity_F9_supply_filter_value"  TEXT,
           
        --filter exhaust
            
           "symbol_G4_exhaust_filter_value"     TEXT,
           "quantity_G4_exhaust_filter_value"   TEXT,
           "symbol_M5_exhaust_filter_value"     TEXT,
           "quantity_M5_exhaust_filter_value"   TEXT,
           "symbol_F7_exhaust_filter_value"     TEXT,
           "quantity_F7_exhaust_filter_value"   TEXT,
           "symbol_F9_exhaust_filter_value"     TEXT,
           "quantity_F9_exhaust_filter_value"   TEXT,
        
            
            
        -- damper
        
           "symbol_supply_damper_value"        TEXT,
        -- heat exchanger
        
           "symbol_exaust_damper_value"        TEXT,
        --heat_exchanger
          
           "symbol_heat_exchanger_value"       TEXT,
        --additional_equipment
           "additional_equipment_value"        TEXT,
        --S_and_p
           "s_and_p_value"                     TEXT
           
   
);
"""

c.execute(query)

conn.commit()
conn.close()