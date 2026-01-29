palabra= input("Ingrese una palabra para buscar: ")
with open("datos.txt") as f:
    cuentas=f.read().count(palabra)
    print(cuentas)