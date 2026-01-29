palabraClave = input("Introduce una palabra clave: ")
palabraClave = palabraClave.lower()
with open("datos.txt") as f:
    for linea in f:
        if palabraClave in linea.lower():
            print(linea)