'''Escribe un programa que lea un archivo CSV llamado datos.csv.csv y muestre
todo su contenido en la consola, fila por fila.'''
import csv
with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)