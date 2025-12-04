from string import whitespace, punctuation, digits, ascii_letters

#Cuenta los caracteres y las vocales en una cadena dada
def contarCaracteres(cadena):
    return len(cadena)

#Cuenta las vocales en una cadena dada
def contarVocales(cadena):
    cadena = cadena.lower()
    return cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u")

#Cuenta las letras en una cadena dada
def contarLetras(cadena):
    return sum(1 for c in cadena if c in ascii_letters)

#contar los números en una cadena dada
def contarNumeros(cadena):
    return sum(1 for c in cadena if c in digits)

#contar los espacios en una cadena dada
def contarEspacios(cadena):
    return sum(1 for c in cadena if c in whitespace)

#contar los puntos en una cadena dada
def contarPuntos(cadena):
    return sum(1 for c in cadena if c in punctuation)