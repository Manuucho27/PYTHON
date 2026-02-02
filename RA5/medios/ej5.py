with open("datos.txt") as f:
    lineas = f.readlines()
    #he intentado borrarlas con un bucle for pero no me ha funcionado

with open("sin_lineas_vacias.txt", "w") as f:
    for linea in lineas:
        if linea.strip():  # Vemos si la línea no está vacía después de eliminar espacios en blanco
            f.write(linea)

with open("sin_lineas_vacias.txt") as f:
    print(f.read())