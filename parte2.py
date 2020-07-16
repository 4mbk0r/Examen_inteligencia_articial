#La media, la moda, la desviación estándar con el uso de numpy y pandas

import numpy as np
import pandas as pd
from scipy import stats
url = 'inteligencia_artificial.csv'
df = pd.read_csv(url, sep=";", encoding='latin-1')
print (df.head())


csv_file = 'inteligencia_artificial.csv'

print ("__________Con PANDAS____________")

#  analizando la variable notas
print ("Promedio de las notas")
print(df["Promedio"].mean())
print ("desviacion estandar de las notas")
print(df["Promedio"].std())
print ("moda de la notas")
print(df["Promedio"].mode())


# analizando la variable promedio
print ("Promedio de los promedios")
print(df["nota"].mean())
print ("desviacion estandar de las promedios")
print(df["nota"].std())
print("moda de los promedios")
print(df["nota"].mode())


# analizando la variable edad
print ("Promedio de las edades")
print ( df["edad"].mean() )
print ("desviacion estandar de la edades")
print (df["edad"].std())
print("moda de los edades")
print(df["edad"].mode())





df = np.genfromtxt(url,delimiter=';')
ans = np.mean(df[1:,5])
stt = np.std(df[1:,5], ddof=1) 

print ("______NUMPY__________")
#  analizando la variable notas
print ("Promedio de las notas")
print(np.mean(df[1:,4]))
print ("desviacion estandar de las notas")
print( np.std(df[1:,4], ddof=1))
print ("moda de la notas")
print(stats.mode(df[1:,4])[0])


# analizando la variable promedio
print ("Promedio de los promedios")
print(np.mean(df[1:,5]))
print ("desviacion estandar de las promedios")
print( np.std(df[1:,5], ddof=1))
print("moda de los promedios")
print(stats.mode(df[1:,5])[0])


# analizando la variable edad
print ("Promedio de las edades")
print(np.mean(df[1:,6]))
print ("desviacion estandar de la edades")
print( np.std(df[1:,6], ddof=1))
print("moda de los edades")
print(stats.mode(df[1:,6])[0])
