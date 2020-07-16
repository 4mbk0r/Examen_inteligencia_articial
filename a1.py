import csv

#La media y la desviación estándar y explique qué 
# significa en cada caso mediante python sin uso de librerías
def media(nombre, columna):
    with open(nombre) as csv_file:
        dataset = csv.reader(csv_file, delimiter=';')
        line_count = 0
        sum=0
        for row in dataset:
            if line_count!=0:
                sum+=int(row[columna])
            line_count+=1
        if(line_count==0):
            return 0
        return sum/(line_count-1)

def _ss(nombre, columna):
    c = media(nombre, columna)
    ss =0
    with open(nombre) as csv_file:
        dataset = csv.reader(csv_file, delimiter=';')
        ss =0
        suma = 0
        i = 0 
        for x in dataset:
            if i!=0:
                suma += (float(x[columna])-float(c))**2
            i+=1 
        ss = (suma/(i-2))**(0.5)
    return ss

csv_file = 'inteligencia_artificial.csv'
#  analizando la variable notas
print ("Promedion de las notas")
print ( media(csv_file,4) )
print ("desviacion estandar de las notas")
print (_ss(csv_file,4))
# analizando la variable promedio
print ("Promedion de los promedios")
print ( media(csv_file,5) )
print ("desviacion estandar de las promedios")
print (_ss(csv_file,5))

# analizando la variable edad
print ("Promedion de las edades")
print ( media(csv_file,6) )
print ("desviacion estandar de la edades")
print (_ss(csv_file,6))



