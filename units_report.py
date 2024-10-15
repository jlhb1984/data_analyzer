import pandas as pd
import numpy as np

class Units_report:
    def __init__(self,table_name):
        self.table_name=table_name

    def create_report(table_name):
        df_books=pd.read_csv(table_name)
        df_books.head(2)
        df_books.info()
        var_filter=input("\nDigita el atributo a buscar: ")
        #En la siguiente línea se puefe agregar los atributos a visualizar, si es uno, no modificar el código.
        df_book_filter01=df_books[['Date',var_filter]]
        print(df_book_filter01) 
        print(df_book_filter01[var_filter].value_counts())
        df_book_filter01.dropna(axis=0,inplace=True)
        Units_report.look_for(df_book_filter01,var_filter)


    def look_for(df_book_filter01,var_filter):
        look_option=input("\nDesea buscar una unidad? S/N\n")
        look_word="w"
        while look_option!='N':
                look_word=input("Digita la unidad a buscar: ")
                filter_df=df_book_filter01[df_book_filter01[var_filter].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Desea buscar una unidad:\nS/N\n")
        exp_option=input("Desea generar un reporte en formato csv?\nS/N\n")
        if (exp_option=='S')&(look_word!='w'):
                filter_df.to_csv('Searched_unit_report.csv')
                look_word='w'
        elif (exp_option=='N'):
             print("Proceso terminado.") 
        
        #units.drop_duplicates(inplace=True)