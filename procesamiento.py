import numpy as np
import pandas as pd
from scipy import stats



def limpieza_de_datos(dataset, lista_eliminar):
    dataset = df.drop(lista_eliminar, axis='columns', inplace=True)
    return  dataset

def datos_faltantes_con_media(dataset, columans, valor):
    
    for x in columans:
        suma = 0
        n =0
        for index, row in df.iterrows():
            if (row[x]!=valor):
                suma+=int(row[x])
                n+=1
        media=suma/n
        dataset[x]=dataset[x].replace({"?":  media  })
    return  dataset


url = 'datasetdeprueaba.csv'
df = pd.read_csv(url, sep=",", encoding='latin-1')
print (df.head())

limpieza_de_datos(df, ['CI', 'Nombrecompleto', 'Departamento'])

print (df.head())

df =  datos_faltantes_con_media(df, ["edad"], "?")

print (df.head())

