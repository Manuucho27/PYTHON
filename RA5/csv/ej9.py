'''Escribe un programa que lea un archivo CSV llamado clientes.csv y busque un
clientes.csv específico por su nombre, mostrando todos los detalles de dicho clientes.csv.'''
import csv
intro=input("¿Que clientes.csv quieres buscar?: ")
with open("clientes.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == intro:
            print(row)