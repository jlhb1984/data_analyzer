import pandas as pd
import numpy as np

class Tables_merger:
    
    def __init__(self,number_of_tables):
        self.number_of_tables=number_of_tables
            
    def merger(number_of_tables):
        table_name=input("Digita el nombre de la tabla: ")
        df_concat=pd.read_csv('TSO Colombia - IBO IDCOM.csv')
        print(df_concat.info())
        print("Unit types: ")
        print(df_concat['Unit Type'])
        #for i in range(0,number_tables):
        #    df_aux=pd.read_csv(table_name)
        #    df_concat=df_concat.concat(df_aux)
        #print(df_concat.info())

    



