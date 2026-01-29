#solucion 1 (correcta)
with open("datos.txt") as f:
    contenido=f.read()
    palabrasCuenta = len(contenido.split())
    print(palabrasCuenta)

#solucion 2 (incorrecta)
with open("datos.txt") as f:
    print(f.read()) #hace que llegue al final
    palabrasCuenta = len((f.read()).split())
    print(palabrasCuenta)

#solucion 3 (correcta)
with open("datos.txt") as f:
    palabrasCuenta = len((f.read()).split())
    print(palabrasCuenta)