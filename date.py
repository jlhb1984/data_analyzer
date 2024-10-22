import pandas as pd

class Date():
    def __init__(self,table02):
        self.table02=table02
    
    def order_date(table02):
        path=table02
        df=pd.read_csv(path)
        df_filter=df[['Unit','Event','Time','GPS Fixed','GPS Age']]
        print(df_filter.info())
        print("Trabajando...")  
        df_filter['Time']=pd.to_datetime(df['Time'])
        print(df_filter.info())              
        df.sort_values(by='Time', ascending=True)
        print(df_filter)
        #df_filter_date=df_filter[(df_filter['Date'].dt.month>8)&(df_filter['Date'].dt.day>26)]
        #print(df_filter_date)
        #print("\n")
        option=input("\nDesea crear un reporte S/N:\n")
        if option=='S':
            df_filter.to_csv('Date ordered.csv')