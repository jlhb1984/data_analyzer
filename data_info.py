import pandas as pd
import numpy as np

class Data_info:
    
    def __init__(self,table_info):
        self.info_table=table_info

    def info(table_info):
        df_table_info=pd.read_csv(table_info)
        missing_data_count=df_table_info.isna().sum()
        print("\nDatos nulos: ")
        print(missing_data_count)
        print("\nInformacíón de la tabla: ")
        print(df_table_info.info())
        total_rows=len(df_table_info)
        print("\nTotal de registros: ")
        print(total_rows)
        option_null=input("Deseas elimianar los datos nulos de la tabla: S/N \n")
        if option_null=="S":
            df_table_info.dropna(axis=0,inplace=True)
            print("\ndf_table_info: ")
            print(df_table_info.info())
            print(df_table_info)
            total_rows=len(df_table_info)
        Data_info.standar(df_table_info,total_rows)

    def standar(df_table_info,total_rows):
        number_of_chars_pn=int(input("\nDigita el número de caracteres a detectar en el campo Phone Number: \n"))
        for i in range(0,total_rows):
            if len(str(df_table_info.iloc[i]['Phone Number']))<number_of_chars_pn:
                print("\nSe encontró registros Phone Number con longitud inferior a la buscada.\n")
                print(df_table_info.iloc[i])
                #df_phone_number=df_table_info.iloc[i]
        number_of_chars_im=int(input("\nDigita el número de caracteres a detectar en el campo IMEI: \n"))
        for j in range(0,total_rows):
            if len(str(df_table_info.iloc[j]['IMEI']))<number_of_chars_im:
                print("\nSe encontró registros IMEI con longitud inferior a la buscada.\n")
                print(df_table_info.iloc[j])
                #df_imei=df_table_info.iloc[j]
        option_drop=input("\nDeseas eliminar los registros que no cumplen la cantidad de caracteres requeridos: S/N \n")
        if option_drop=='S':
            print(total_rows)
            print(df_table_info.info()) 
            df_table_info_aux=df_table_info
           
            for i in range(0,total_rows):
                if len(df_table_info.iloc[i]['Phone Number'])<number_of_chars_pn:
                    df_table_info_aux=df_table_info_aux.drop(i)
            #df_table_info=df_table_info_aux
            total_rows=len(df_table_info_aux)
            df_table_info_aux_f=df_table_info_aux
            for i in range(0,total_rows):
                if (len(str(df_table_info_aux.iloc[i]['IMEI'])))<number_of_chars_im:
                    df_table_info_aux_f=df_table_info_aux_f.drop(i)

        print(df_table_info_aux_f.info())                 
        
                    