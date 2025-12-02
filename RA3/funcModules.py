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


def calcular_precio(precio_base: float, *, iva: float = 21):
    precio_final = precio_base * (1 + iva / 100)
    return precio_final


usuarios = []
def crear_usuario(*, nombre: str, email: str, activo: bool = True):
    usuarios.append((nombre, email, activo))
    usuariosActivos = []
    for usuario in usuarios:
        if usuario[2] == True:
            usuariosActivos.append(usuario)
    return usuariosActivos


def formatear_nombre(nombre: str, apellido: str, *, orden: str = "nombre_apellido",):
    if orden == "nombre_apellido":
        return f"{nombre} {apellido}"
    elif orden == "apellido_nombre":
        return f"{apellido} {nombre}"
    else:
        return "Error: el valor de 'orden' debe ser 'nombre_apellido' o 'apellido_nombre'."


def calcular_descuento(precio_original: float, *, descuento: float = 10):
    precio_final = precio_original * (1 - descuento / 100)
    return precio_final


def filtrar_pares(numeros: list[int]):
    pares = [n for n in numeros if n % 2 == 0]
    return pares

def tabla_multiplicar(numero: int, *, hasta: int = 10):
    tabla = [numero * i for i in range(1, hasta + 1)]
    return tabla


def maximo(*numeros: int):
    if not numeros:
        return None
    return max(numeros)

def sumatorio(*numeros: int):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado

def multiplicador(*numeros: int, multiplicador: int = 1):
    resultado = 0
    for n in numeros:
        suma=n * multiplicador
        resultado += suma
        print(f"Resultado de {n} x {multiplicador} =",suma)
    return resultado

def multiplicadorSumatorio(*numeros: int, multiplicador: int = 1):
    resultado = 0
    resultado += sumatorio(*numeros)*multiplicador
    return resultado


def makePizza(nombrePizza:str, *ingredientes:str, porciones:int = 8):
    return (f"Pizza '{nombrePizza}' incluye los siguientes ingredientes: {', '.join(ingredientes)}"
            f"\nPartida en {porciones} porciones\n")

def ganador(*nombres: str, premio:int = 1000):
    if len(nombres) == 1:
        return f"El ganador es {nombres[0]}, has ganado {premio}€!"
    else:
        ran= random.randrange(len(nombres))
        # random.randint(0, len(nombres) - 1)
        return f"El ganador es {nombres[ran]}, has ganado {premio}€!"


# funcion para calcular el precio de una entrada (precioEntrada()), sabiendo que para
# ello deberemos conocer el precio normal de la entrada (por defecto 10)
# necesitamos conocer la edad del asistente y si es o no estudiante
# si es menor y/o estudiante tendrá un descuento del 10%

def precioEntradas(precio: float = 10, *, edad: int, estudiante:bool):
    if estudiante or edad < 18:
        precio -= (precio * 0.1)
    return precio


def fibonacci(n):
    if n <= 1:               # caso base
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # llamada doble recursiva
