import csv

lista_datos = [
    ['Zipi','García','12345678A','25'],
    ['Zape','López','23456789B','32']
]
lista_diccionario = [
    {'Nombre': 'Juan', 'dni': '20497865'},
    {'Nombre': 'Ana', 'dni': '2245678'},
    {'Nombre': 'Luis', 'dni': '21173478'}
]

#1.- Leer CSV como archivo de texto
print("Leer CSV como archivo de texto\n")
with open("datos.csv", "r") as f:
    for linea in f:
        print(linea.strip())



#2.- Leer CSV con módulo CSV integrado en Python
print("\nLeer CSV con módulo CSV integrado en Python (listas)\n")
with open("datos.csv", "r") as f:
    lector = csv.reader(f) # delimiter=";" por defecto
    next(lector) #-- se salta el encabezado
    for linea in lector:
        print(linea)


#3.- Leer CSV como diccionario
print("\nLeer CSV como diccionario\n")
with open("datos.csv", "r") as f:
    lector = csv.DictReader(f)
    next(lector)
    for linea in lector:
        print(linea)

    #Leer sólo las columnas que necesite nombre y dni
    f.seek(0) #volvemos al principio del fichero

    for linea in lector:
        print(linea["nombre"], linea["dni"])


#4.- Añadir datos CSV con módulo CSV integrado en Python
with open("datos.csv", "a") as f:
    escritor = csv.writer(f)
    escritor.writerow(['Mary', 'Lopez', '12345678A', '25'])
    escritor.writerow(['Oscar', 'Lopez', '12345678A', '25'])
    escritor.writerows(lista_datos)

#5.-Excribir en el fichero CSV
with open("datos2.csv", "w") as f:
    escritor = csv.DictWriter(f, fieldnames=["Nombre", "dni"])
    #escritor.writeheader()
    escritor.writerows(lista_diccionario)