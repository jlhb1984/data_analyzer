import pandas as pd
import numpy as np

class Tables_merger:
    
    def __init__(self,number_of_tables):
        self.number_of_tables=number_of_tables
            
    def merger(number_of_tables):
               
        if number_of_tables==1:
            table_name=input("\nDigita el nombre de la tabla 1:")
            df=pd.read_csv(table_name)          
            df_unit_types=df['Unit Type']
            print(df_unit_types)
        
        elif number_of_tables>1:
            table_name=input("\nDigita el nombre de la tabla 1:")
            df=pd.read_csv(table_name)
            df_unit_types=df['Unit Type']
            print("\nUnits en table 1:\n",df_unit_types)
                        
            for i in range(1,number_of_tables):
                table_name=input("\nDigita el nombre de la tabla:")
                df_aux=pd.read_csv(table_name)
                df_aux_unit_types=df_aux['Unit Type']
                print("\nUnite types before concat:\n",df_unit_types.info())
                df_concat=pd.concat([df_unit_types,df_aux_unit_types],axis=0)
                print("\nUnite types after concat:\n")
                print(df_concat.info())   



