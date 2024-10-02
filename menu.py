import pandas as pd
import numpy as np
from tables_comparator import Tables_comparator
from data_analyzer import Data_analyzer
from units_report import Units_report

print("data_analyzer.")
option=input("1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Salir. \n")

while option!=4:
    
    if option=='1':
        number_plate=input("Digite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)

    elif option=='2':
        #Carga de la tabla 1. Landmarks InOut.csv
        table01=input("Digita el nombre de la tabla 1: ")
        df_book_landmarks=pd.read_csv(table01)
        df_book_landmarks.info()

        #Carga de la tabla 2. Geofences InOut Report.csv
        table02=input("Digita el nombre de la tabla 2: ")
        df_book_geofences=pd.read_csv(table02)
        df_book_geofences.info()

        #Carga de la columna de la tabla 1. ContactName
        table01_column=input("Digita el nombre de la columna de la tabla 1: ")
        landmarks=df_book_landmarks.loc[:,table01_column]
        landmarks.info()
        print(landmarks)

        #Carga de la columna de la tabla 1. GeofenceName
        table02_column=input("Digita el nombre de la columna de la tabla 2: ")
        geofences=df_book_geofences.loc[:,table02_column]
        geofences.info()
        print(geofences)

        Tables_comparator.comparator(landmarks,geofences)

    elif option=='3':
        #Carga de la tabla. Customer-Units.csv
        table_name=input("Digita el nombre de la tabla: ")
        Units_report.create_report(table_name)       

    elif option=='4':
        print("Saliendo")
        break
    
    option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Units report. \n4. Salir. \n")
