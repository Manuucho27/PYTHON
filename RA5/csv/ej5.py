'''Escribe un programa que cree un archivo CSV llamado productos.csv.csv y escriba en
él los nombres de productos.csv, sus precios y cantidades en stock.'''
import csv
productos = [{"Manzana","1.50","100"}, {"Banana","0.80","150"},{"Naranja","0.90","120"}]
with open("productos.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(productos)

with open("productos.csv") as f:
    print(f.read())