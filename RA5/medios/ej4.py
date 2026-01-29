palabraBuscada = input("Introduce una palabra: ").lower()
palabraNueva = input("Introduce una palabra nueva: ").lower()

with open("datos.txt") as f:
    contenido = f.read().replace(palabraBuscada, palabraNueva)

with open("modificado.txt", "w") as f:
    f.write(contenido)