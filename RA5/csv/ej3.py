'''Escribe un programa que lea un archivo CSV llamado datos.csv y muestre
solo los valores de la columna “Nombre”.'''
import csv
with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])