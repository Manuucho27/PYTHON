with open("datos.txt") as f:
    lineas = f.readlines()

with open("copia.txt", "w") as f:
    f.writelines(lineas)