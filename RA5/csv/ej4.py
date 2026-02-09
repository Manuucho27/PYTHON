'''Crea un programa que lea un archivo CSV llamado notas.csv y
calcule el promedio de las notas que se encuentran en la columna “Nota”.'''
import csv
notas = []
with open("notas.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        notas.append(float(row[1]))
print( round( sum(notas)/len(notas) , 2 ) )