'''Crea un programa que escriba varios registros de estudiantes en un archivo CSV
llamado estudiantes.csv utilizando csv.DictWriter().'''
import csv

estudiantes = [
    {'Nombre': 'Juan', 'Edad': '20', 'Grado': 'A'},
    {'Nombre': 'Ana', 'Edad': '22', 'Grado': 'B'},
    {'Nombre': 'Luis', 'Edad': '21', 'Grado': 'A'}
]

with open('estudiantes.csv', 'w', newline='') as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=['Nombre', 'Edad', 'Grado'])
    escritor.writeheader()
    escritor.writerows(estudiantes)

with open('estudiantes.csv') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for estudiante in lector:
        print(estudiante)