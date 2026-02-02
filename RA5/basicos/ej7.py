with open("datos.txt") as f:
    lineas = f.readlines()

invertido = lineas[::-1]
with open("copia.txt", "w") as f:
    f.writelines(invertido)

with open("copia.txt") as f:
    print(f.read())