import pandas as pd
import numpy as np

class Units_report:
    def __init__(self,table_name):
        self.table_name=table_name

    def create_report(table_name):
        df_books=pd.read_csv(table_name)
        df_books.head(2)
        units=d=df_books[['Unit Type']]
        units.drop_duplicates(inplace=True)
        print(units)
        units.to_csv('Units.csv',index=False)