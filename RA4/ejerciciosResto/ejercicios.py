#Modifica la cadena “ este ejercicio es muy complicado ” para que el ejercicio
#sea facilísimo y cada una de las palabras comience en mayúsculas y sin espacios y luego
#imprimelo invertido, ademas busca el indice de la palabra complicado.

print("_ Ejercicio 1 _")
cadena = "        Este ejercicio es muy complicado         "
cadena = cadena.title()
cadena = cadena.replace(" ", "")
print(cadena.index("Complicado"))
cadena = cadena.replace("Complicado", "Facilisimo")
print(cadena)
print(cadena[::-1])

print("")
#Vamos a definir una cadena y la vamos a pasar a minúsculas, eliminar los espacios
#y las letras pares las vamos a cambiar por asteriscos
print("_ Ejercicio 2 _")
cadena = "Este ejercicio es muy complicado"
cadena = cadena.lower().replace(" ", "")
cadena = "".join(["*" if i % 2 == 0 else c for i, c in enumerate(cadena)])
print(cadena)

print("")
#Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas reglas:
#- Palabras que empiezan por vocal.
#- Palabras que terminan en consonante.
#- Palabras que contienen algún número.
#El programa debe:
#- Separar el texto en palabras.
#- Detectar cuáles cumplen cada condición.
#- Guardarlas en un diccionario con tres listas.
#- Mostrar un informe final indicando las palabras encontradas en cada categoría y cuántas hay en cada una
print("_ Ejercicio 3 _")
texto = input("Introduce un texto: ")
palabras = texto.split()
categorias = {
    "vocal": [],
    "consonante": [],
    "numero": []
}
for palabra in palabras:
    if palabra[0].lower() in "aeiou":
        categorias["vocal"].append(palabra)
    if palabra[-1].lower() not in "aeiou":
        categorias["consonante"].append(palabra)
    if any(caracter.isdigit() for caracter in palabra):
        categorias["numero"].append(palabra)
print("Informe final:")
for categoria, lista in categorias.items():
    print(f"Palabras que {categoria}: {lista} (Total: {len(lista)})")

print("")
#Crea una función que reciba un argumento string y compruebe si todos los caracteres son mayúsculas
print("_ Ejercicio 4 _")
def son_todas_mayusculas(texto):
    return texto.isupper()
texto = input("Introduce un texto: ")
print(son_todas_mayusculas(texto))

print("")
#A través de una función, introduciendo una cadena por parámetro, devolver la longitud, devolver
#la cadena en minúsculas y devolver las ultimas 5 letras de la cadena.
print("_ Ejercicio 5 _")
def cadena_completa(cadena):
    letras = "".join(cadena.split())
    return len(cadena), cadena.lower(), letras[-5:]

cadena = input("Introduce una cadena: ")
minusculas=cadena_completa(cadena)[1]
ultimas_cinco=cadena_completa(cadena)[2]
print(f"Longitud: {cadena_completa(cadena)[0]}")
print(f"Minusculas: {minusculas}")
print(f"Ultimas cinco letras: {ultimas_cinco}")

print("")
#Recoger un email por consola introducido por el usuario. En una función se debe comprobar que
#el correo introducido por el usuario contenga “@” y acabe en “.com” o “.es”. Además, el usuario
#solo tendrá tres oportunidades para validar el correo.
print("_ Ejercicio 6 _")
def validar_correo(correo):
    return correo.count("@") == 1 and correo.endswith((".com", ".es"))
intentos = 3
while intentos > 0:
    correo = input("Introduce un correo electrónico: ")
    if validar_correo(correo):
        print("Correo válido.")
        break
    else:
        intentos -= 1
        print(f"Correo inválido. Te quedan {intentos} intentos.")
if intentos == 0:
    print("Has agotado tus intentos.")

print("")
#Pida al usuario una frase.
#Elimine los espacios al inicio y al final (strip()).
#Muestre: La frase en minúsculas (lower()).
#La frase en mayúsculas (upper()).
#La frase con la primera letra en mayúscula (capitalize()).
#Reemplace todas las comas por puntos (replace()).
#Cuente cuántas veces aparece una palabra que el usuario ingresa (count()).
#Verifique si la frase empieza con una vocal (startswith()).
#Muestre cuántas palabras tiene la frase (split()).
print("_ Ejercicio 8 _")
