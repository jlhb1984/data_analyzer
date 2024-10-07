import pandas as pd
import numpy as np
from tables_comparator import Tables_comparator
from data_analyzer import Data_analyzer
from units_report import Units_report
from tables_merger import Tables_merger

print("data_analyzer.")
option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Merger. \n5. Table_info. \n6. Salir. \n")

while option!='6':
    
    if option=='1':
        number_plate=input("\nDigite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)

    elif option=='2':
        #Carga de la tabla 1. Landmarks InOut.csv
        table01=input("\nDigita el nombre de la tabla 1: ")
        df_book_landmarks=pd.read_csv(table01)
        df_book_landmarks.info()

        #Carga de la tabla 2. Geofences InOut Report.csv
        table02=input("\nDigita el nombre de la tabla 2: ")
        df_book_geofences=pd.read_csv(table02)
        df_book_geofences.info()

        #Carga de la columna de la tabla 1. ContactName
        table01_column=input("\nDigita el nombre de la columna de la tabla 1: ")
        landmarks=df_book_landmarks.loc[:,table01_column]
        landmarks.info()
        print(landmarks)

        #Carga de la columna de la tabla 1. GeofenceName
        table02_column=input("\nDigita el nombre de la columna de la tabla 2: ")
        geofences=df_book_geofences.loc[:,table02_column]
        geofences.info()
        print(geofences)

        Tables_comparator.comparator(landmarks,geofences)

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
        df_table_info=pd.read_csv(table_info)
        missing_data_count=df_table_info.isna().sum()
        print("\nDatos nulos: ")
        print(missing_data_count)
        print(df_table_info.info())
        total_rows=len(df_table_info)
        print("Total de registros: ")
        print(total_rows)
        count_can_ventas=0
        count_IMEI_empty=0
        
        for i in range(0,total_rows):
            #print(df_table_info.iloc[i]['Company'])
            if df_table_info.iloc[i]['Company']=='**CANCELADO VENTAS':
                count_can_ventas=count_can_ventas+1
            #elif df_table_info.iloc[i]['IMEI']==None:
            #    count_IMEI_empty=count_IMEI_empty+1       
            
        print("\nCompany=**CANCELADO VENTAS:")
        print(count_can_ventas)
        #print("\nIMEI=' '")
        #print(count_IMEI_empty)
        count_can_ventas=0
        count_IMEI_empty=0
        
    elif option=='6':
        print("Saliendo")
        break
    
    option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Merger. \n5. Table_info. \n6. Salir. \n")
