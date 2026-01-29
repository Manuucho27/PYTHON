numAparicionesPorPalabra = {}
with open("datos.txt") as f:
    palabras = f.read().split()
    for palabra in palabras:
        numAparicionesPorPalabra[palabra] = palabras.count(palabra)
print(numAparicionesPorPalabra)