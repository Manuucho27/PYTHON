with open("datos.txt") as f:
    lineas = f.readlines()
    lineaLarga = ""
    lineaCorta = ""

    for i in range(len(lineas)):
        if i == 0:
            lineaLarga = lineas[i]
            lineaCorta = lineas[i]
        else:
            if len(lineas[i]) > len(lineaLarga):
                lineaLarga = lineas[i]
            if len(lineas[i]) < len(lineaCorta):
                lineaCorta = lineas[i]

    print("Linea más larga: ", lineaLarga)
    print("Linea más corta: ", lineaCorta)