import pandas as pd
import numpy as np
from tables_comparator import Tables_comparator
from data_analyzer import Data_analyzer
from units_report import Units_report
from tables_merger import Tables_merger
from data_info import Data_info
from date import Date

print("data_analyzer.")
option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Merger. \n5. Table_info. \n6. Messages. \n7. Str_date_order  \n8. Salir. \n")

while option!='8':
    
    if option=='1':
        number_plate=input("\nDigite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)

    elif option=='2':
        #Carga de la tabla 1. Landmarks InOut.csv
        table01=input("\nDigita el nombre de la tabla 1: ")
        df_book_table01=pd.read_csv(table01)
        df_book_table01.info()

        #Carga de la tabla 2. Geofences InOut Report.csv
        table02=input("\nDigita el nombre de la tabla 2: ")
        df_book_table02=pd.read_csv(table02)
        df_book_table02.info()

        #Carga de la columna de la tabla 1. ContactName
        table01_column=input("\nDigita el nombre de la columna de la tabla 1: ")
        atribute_table01=df_book_table01.loc[:,table01_column]
        atribute_table01.info()
        print(atribute_table01)

        #Carga de la columna de la tabla 1. GeofenceName
        table02_column=input("\nDigita el nombre de la columna de la tabla 2: ")
        atribute_table02=df_book_table02.loc[:,table02_column]
        atribute_table01.info()
        print(atribute_table02)

        Tables_comparator.comparator(atribute_table01,atribute_table02)

    elif option=='3':
        #Carga de la tabla. Customer-Units.csv
        table_name=input("\nDigita el nombre de la tabla: ")
        Units_report.create_report(table_name)

    elif option=='4':
        #carga de las tablas a fusionar.
        number_of_tables=int(input("\nDigita el número de tablas: "))
        Tables_merger.merger(number_of_tables)

    elif option=='5':
        table_info=input("\nDigita el nombre de la tabla: ")
        Data_info.info(table_info)
    
    elif option=='6':
        message=input("\nDigita la cadena: ")
        print("\nLongitud de la cadena: ",len(message))

    elif option=='7':
        table02=input("Digita el nombre de la tabla: ")
        Date.order_date(table02)          
  
    elif option=='8':
        print("Saliendo")
        break
    
    option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Merger. \n5. Table_info. \n6. Messages. \n7. Str_date_order  \n8. Salir. \n")
