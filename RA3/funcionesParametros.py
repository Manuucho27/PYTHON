import random


def saludar(*, nombre: str, saludo: str = "Hola"):
    return f"{saludo} {nombre}"

def saludoAleatorio(saludo: str, *nombre:str, **kwargs):
    ran= random.randint(0, len(nombre) - 1)
    if "ciudad" in kwargs:
        return f"{saludo} {nombre[ran]}, vamos a {kwargs['ciudad']}!"
    if "hijos" in kwargs:
        return f"{saludo} {nombre[ran]}, tienes {kwargs['hijos']} hijos!"
    return f"{saludo} {nombre[ran]}"

print("EJERCICIO 1:")
print(saludar(nombre="Juan"))
print(saludar(saludo="Buenos dias", nombre="Juan"))
print(saludoAleatorio("Buenos dias", "Juan", "Rafa", "Manu", ciudad="Madrid", hijos=3))


def calcular_precio(precio_base: float, *, iva: float = 21):
    precio_final = precio_base * (1 + iva / 100)
    return precio_final

print("EJERCICIO 2:")
print(calcular_precio(100))
print(calcular_precio(100, iva=18))

usuarios = []
def crear_usuario(*, nombre: str, email: str, activo: bool = True):
    usuarios.append((nombre, email, activo))
    usuariosActivos = []
    for usuario in usuarios:
        if usuario[2] == True:
            usuariosActivos.append(usuario)
    return usuariosActivos

print("EJERCICIO 3:")
print(crear_usuario(nombre="Juan", email=""))
print(crear_usuario(nombre="Manu", email="", activo=True))
print(crear_usuario(nombre="Rafa", email="", activo=False))
print(crear_usuario(nombre="Rafa", email="", activo=True))


def formatear_nombre(nombre: str, apellido: str, *, orden: str = "nombre_apellido",):
    if orden == "nombre_apellido":
        return f"{nombre} {apellido}"
    elif orden == "apellido_nombre":
        return f"{apellido} {nombre}"
    else:
        return "Error: el valor de 'orden' debe ser 'nombre_apellido' o 'apellido_nombre'."

print("EJERCICIO 4:")
print(formatear_nombre("Juan", "Perez"))
print(formatear_nombre("Juan", "Perez", orden="apellido_nombre"))


def calcular_descuento(precio_original: float, *, descuento: float = 10):
    precio_final = precio_original * (1 - descuento / 100)
    return precio_final

print("EJERCICIO 5:")
print(calcular_descuento(100))
print(calcular_descuento(100, descuento=20))


def filtrar_pares(numeros: list[int]):
    pares = [n for n in numeros if n % 2 == 0]
    return pares

print("EJERCICIO 6:")
print(filtrar_pares([1, 2, 3, 4, 5]))

def tabla_multiplicar(numero: int, *, hasta: int = 10):
    tabla = [numero * i for i in range(1, hasta + 1)]
    return tabla

print("EJERCICIO 7:")
print(tabla_multiplicar(5))
print(tabla_multiplicar(5, hasta=15))


def maximo(*numeros: int):
    if not numeros:
        return None
    return max(numeros)

print("EJERCICIO 8:")
print(maximo(1, 2, 3, 4, 5))
print(maximo(1, 2, 3, 4, 5, 6))
print(maximo())

def sumatorio(*numeros: int):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado

print("EJERCICIO 9:")
print(sumatorio(1, 2, 3, 4, 5))
print(sumatorio(1, 2, 3, 4, 5, 6))
print(sumatorio())

def multiplicador(*numeros: int, multiplicador: int = 1):
    resultado = 0
    for n in numeros:
        suma=n * multiplicador
        resultado += suma
        print(f"Resultado de {n} x {multiplicador} =",suma)
    return resultado

print("EJERCICIO 10:")
print(multiplicador(1, 2, 3, 4, 5))
print(multiplicador(1, 2, 3, 4, 5, multiplicador=2))
print(multiplicador(1, 2, 3, 4, 5, 6, multiplicador=3))
print(multiplicador())


def multiplicadorSumatorio(*numeros: int, multiplicador: int = 1):
    resultado = 0
    resultado += sumatorio(*numeros)*multiplicador
    return resultado

print("EJERCICIO 11:")
print(multiplicadorSumatorio(1, 2, 3, 4, 5))
print(multiplicadorSumatorio(1, 2, 3, 4, 5, multiplicador=2))
print(multiplicadorSumatorio(1, 2, 3, 4, 5, 6, multiplicador=3))
print(multiplicadorSumatorio())


def makePizza(nombrePizza:str, *ingredientes:str, porciones:int = 8):
    return (f"Pizza '{nombrePizza}' incluye los siguientes ingredientes: {', '.join(ingredientes)}"
            f"\nPartida en {porciones} porciones\n")

print("EJERCICIO 12:")
print(makePizza("Manu Pizza", "pepperoni", "tomate", porciones=7))
print(makePizza("Pepperoni", "pepperoni" , "tomate", "queso", porciones=16))
print(makePizza("Rafa Pizza", "tomate", "queso"))


def ganador(*nombres: str, premio:int = 1000):
    if len(nombres) == 1:
        return f"El ganador es {nombres[0]}, has ganado {premio}€!"
    else:
        ran= random.randrange(len(nombres))
        # random.randint(0, len(nombres) - 1)
        return f"El ganador es {nombres[ran]}, has ganado {premio}€!"

print("EJERCICIO 13:")
print(ganador("Juan", "Rafa", "Manu", premio=10))