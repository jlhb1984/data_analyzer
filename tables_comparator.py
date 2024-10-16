import pandas as pd
import numpy as np

class Tables_comparator:
    def __init__(self,atribute_table01,atribute_table02):
        self.atribute_table01=atribute_table01
        self.atribute_table02=atribute_table02
             
    def comparator(atribute_table01,atribute_table02):
        atribute_table01.drop_duplicates(inplace=True)
        atribute_table02.drop_duplicates(inplace=True)
        total_atribute01=atribute_table01.count()
        total_atribute02=atribute_table02.count()
        print("Total atribute_table01: ",total_atribute01)
        print("Total atribute_table02: ",total_atribute02)
        print("Buscando campos iguales en tabla1 y tabla 2...")
        for i in range(0,total_atribute01):
            for j in range(0,total_atribute02):
                if atribute_table01.iloc[i]==atribute_table02.iloc[j]:
                    print("Campo: ",i,"con valor de: ",atribute_table01.iloc[i],". ","Campo: ",j,"con valor de: ",atribute_table02.iloc[j],".")