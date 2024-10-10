import pandas as pd
import numpy as np

class Units_report:
    def __init__(self,table_name):
        self.table_name=table_name

    def create_report(table_name):
        df_books=pd.read_csv(table_name)
        df_books.head(2)
        df_books.info()
        #var_filter=input("\nDigita el atributo a buscar: ")
        df_book_filter01=df_books[['Unit','Owner','Assigned To']]
        print(df_book_filter01)
        #units.drop_duplicates(inplace=True)