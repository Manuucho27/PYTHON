import math


#Crea una función calcular_estadisticas(numeros) que reciba una lista de
#números y devuelva una tupla con:
#valores mínimo y máximo y la media aritmética
def calcular_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

lista=[1, 2, 3, 4, 5]
print(f'Las estádisitcas de {lista} son:\n'
      f'Valor mínimo: {calcular_estadisticas(lista)[0]}\n'
      f'Valor máximo: {calcular_estadisticas(lista)[1]}\n'
      f'Valor medio: {calcular_estadisticas(lista)[2]}')
print("")

#Crea una función distancia(p1, p2) que reciba dos tuplas representando
#puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
p1= (1, 2)
p2= (4, 6)
print(f"La distancia entre los puntos ({p1}) y ({p2}) es: {distancia(p1, p2)}")
print("")

#Crea una función analizar_texto(texto) que devuelva una tupla con:
#num total de caracteres, num de palabras y la primera palabra
def analizar_texto(texto):
    return len(texto), texto.count(" "), texto.split()[0]
texto="Hola mundo"
print(f"El texto {texto} tiene: {analizar_texto(texto)}")
print("")

#Crea una función convertir_temperatura(celsius) que reciba una
#temperatura en grados Celsius y devuelva una tupla con:
#la temperatura en grados Fahrenheit y la temperatura en Kelvin
def convertir_temperatura(celsius):
    return (celsius * 9/5) + 32, celsius + 273.15
print(f"La temperatura en grados Fahrenheit es: {convertir_temperatura(20)[0]}")
print(f"La temperatura en Kelvin es: {convertir_temperatura(20)[1]}")
print("")

#Crea una función analizar_numeros(numeros) que reciba una lista de
#enteros y devuelva una tupla con:
#num de elementos pares, num de impares y la suma total
def analizar_numeros(numeros):
    impares=0
    pares=0
    for n in numeros:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares, sum(numeros)
lista=[1, 2, 3, 4, 5, 6]
print(f'En la lista {lista} hay:\n'
      f'Números pares: {analizar_numeros(lista)[0]}\n'
      f'Números impares: {analizar_numeros(lista)[1]}\n'
      f'Suma total: {analizar_numeros(lista)[2]}')
print("")

#Crea una función procesar_cadena(cadena) que devuelva una tupla con:
#la cadena en mayus, la cadena en minusc y su longitud
def procesar_cadena(cadena):
    return cadena.upper(), cadena.lower(), len(cadena)
cadena="Hola Mundo"
print(f'La cadena "{cadena}" procesada es:\n'
      f'En mayúsculas: {procesar_cadena(cadena)[0]}\n'
      f'En minúsculas: {procesar_cadena(cadena)[1]}\n'
      f'Longitud: {procesar_cadena(cadena)[2]}')