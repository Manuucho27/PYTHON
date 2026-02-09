'''Escribe un programa que lea un archivo CSV llamado clientes.csv y busque un
clientes.csv específico por su nombre, mostrando todos los detalles de dicho clientes.csv.'''
import csv
intro=input("¿Que clientes.csv quieres buscar?: ")
guardar=[]
with open("clientes.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == intro:
            print(row)
            guardar.append(row)

with open("guardar.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(guardar)