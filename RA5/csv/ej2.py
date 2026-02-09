'''Escribe un programa que lea un archivo CSV llamado datos.csv y cuente cuántas
filas tiene, excluyendo la fila de cabecera.'''
import csv

with open('datos.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    encabezado = next(lector)  # Saltar la primera fila (cabecera)
    total_filas = sum(1 for fila in lector)

print(f"El archivo tiene {total_filas} filas (sin contar la cabecera).")