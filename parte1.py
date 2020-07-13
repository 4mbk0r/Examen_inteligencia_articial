import csv


def cargar_csv(nombre):
    with open(nombre) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        return csv_reader



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
print ( media(csv_file,5) )
print (_ss(csv_file,5))


#La media y la desviación estándar y explique qué 


# significa en cada caso mediante python sin uso de librerías
