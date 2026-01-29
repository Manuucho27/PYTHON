try:
    f = open("datos.txt")
    print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")