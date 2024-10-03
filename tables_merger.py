import pandas as pd
import numpy as np

class Tables_merger:
    
    def __init__(self,number_of_tables):
        self.number_of_tables=number_of_tables
            
    def merger(number_of_tables):       
               
        if number_of_tables==1:
            table_name=input("\nDigita el nombre de la tabla 1:")
            df=pd.read_csv(table_name)          
            df_unit_types=df[['Unit Type','IMEI','Company','Phone Number','Last Event Date']]
            print(df_unit_types)

            Tables_merger.csv_reports(df_unit_types)
            """
            exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
            if (exp_option=="S"):
                df_unit_types.to_csv('Unit_searched_report_units.csv')
            
            look_option=input("Desea buscar una unidad:\nS/N\n")
            while look_option!='N':
                look_word=input("Digita la unidad a buscar: ")
                filter_df=df_unit_types[df_unit_types['Unit Type'].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Desea buscar una unidad:\nS/N\n")

            exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
            if (exp_option=="S"):
                filter_df.to_csv('Unit_searched_report_units.csv')            
            """
        
        elif number_of_tables>1:
            table_name=input("\nDigita el nombre de la tabla 1:")
            df=pd.read_csv(table_name)
            print("Información del dataframe: ")
            print(df.info())
            df_unit_types=df[['Unit Type','IMEI','Company','Phone Number','Last Event Date']]
            #print("\nUnits en table 1:")
            #print(df_unit_types)
                        
            for i in range(1,number_of_tables):
                #UTS Sistemas Kalo MX.csv
                #TSO Colombia - IBO IDCOM.csv
                #TSO Colombia - IBO SEGTEC.csv
                #TSO Mobile - Colombia.csv
                #TSO Mobile - Peru.csv
                #TSO Peru - FG SATELITAL.csv
                table_name=input("\nDigita el nombre de la tabla:")
                df_aux=pd.read_csv(table_name)
                df_aux_unit_types=df_aux[['Unit Type','IMEI','Company','Phone Number','Last Event Date']]
                print("\nUnite types before concat:",df_unit_types.info())
                print("\n")
                df_unit_types=pd.concat([df_unit_types,df_aux_unit_types],axis=0)
                print("\nUnite types after concat:")
                print("\n")
                print(df_unit_types.info()) 
                #print(df_unit_types)
            
            Tables_merger.csv_reports(df_unit_types)
            """
            exp_option=input("Desea generar un reporte en formato csv?\nS/N\n")
            if (exp_option=="S"):
                df_unit_types.to_csv('Report_units.csv')

            look_option=input("Desea buscar una unidad:\nS/N\n")
            
            while look_option!='N':
                look_word=input("Digita la unidad a buscar: ")
                filter_df=df_unit_types[df_unit_types['Unit Type'].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Desea buscar una unidad:\nS/N\n")
            
            exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
            if (exp_option=="S"):
                filter_df.to_csv('Unit_searched_report_units.csv')
            """

    def csv_reports(df):       
       df_unit_types=df[['Unit Type','IMEI','Company','Phone Number','Last Event Date']]
       print(df_unit_types)
       exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
       if (exp_option=="S"):
            df_unit_types.to_csv('Unit_searched_report_units.csv')
       look_option=input("Desea buscar una unidad:\nS/N\n")
       while look_option!='N':
                look_word=input("Digita la unidad a buscar: ")
                filter_df=df_unit_types[df_unit_types['Unit Type'].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Desea buscar una unidad:\nS/N\n")
       exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
       if (exp_option=="S"):
                filter_df.to_csv('Unit_searched_report_units.csv')  