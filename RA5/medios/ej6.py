with open("datos.txt") as f:
    lineas = f.readlines()

#ordenar las lineas alfabeticamente
lineas.sort()

with open("ordenado.txt", "w") as f:
    f.writelines(lineas)

with open("ordenado.txt") as f:
    print(f.read())