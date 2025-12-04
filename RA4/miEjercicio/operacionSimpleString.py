#Cuenta caracteres de una cadena
def contarLetras(texto):
    contador = 0
    for c in texto:
        if c.isalpha():
            contador += 1
    return contador

#Cuenta los números de una cadena
def contarNumeros(texto):
    contador = 0
    for c in texto:
        if c.isdigit():
            contador += 1
    return contador

#Cuenta los espacios de una cadena
def contarEspacios(texto):
    contador = 0
    for c in texto:
        if c == " ":
            contador += 1
    return contador

#Cuenta los signos de puntuación de una cadena
def contarPuntos(texto):
    contador = 0
    for c in texto:
        if not (c.isalpha() or c.isdigit() or c == " "):
            contador += 1
    return contador