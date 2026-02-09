'''Crea un programa que añada nuevas filas de datos a un archivo CSV llamado inventario.csv.
Las nuevas filas deben incluir los datos de productos.csv adicionales.
No se puede añadir si el num de unidades es menor que 10'''
import csv
with open("inventario.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Precio", "Unidades"])
    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == "salir":
            break
        precio = float(input("Ingrese el precio del producto: "))
        unidades = int(input("Ingrese el número de unidades: "))
        if unidades < 10:
            print("No se puede añadir el producto. El número de unidades debe ser al menos 10.")
            continue
        writer.writerow([producto, precio, unidades])

with open("inventario.csv", "r") as f:
    print(f.read())