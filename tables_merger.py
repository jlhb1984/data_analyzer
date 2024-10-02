import pandas as pd
import numpy as np

class Tables_merger:
    
    def __init__(self,number_tables):
        self.number_tables=number_tables
            
    def merger(number_tables):
        table_name=input("Digita el nombre de la tabla: ",i+1)
        df_concat=pd.read_csv('table_name')
        for i in range(0,number_tables):
            df_aux=pd.read_csv('table_name')
            df_concat=df_concat.concat(df_aux)
        print(df_concat.info())

    



