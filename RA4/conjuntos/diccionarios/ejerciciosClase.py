def ej_1():
    '''Escribir un programa que guarde en una variable
    el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
    pregunte al usuario por una divisa y muestre su símbolo
    o un mensaje de aviso si la divisa no está en el diccionario.'''

    def da_divisa(divisa):
        divisa = divisa.strip()
        divisa = divisa.capitalize()
        divisas = {'Euro':'€',
                   'Dollar':'$',
                   'Yen':'¥'}
        if divisa in divisas:
            return f"El símbolo del {divisa} es {divisas[divisa]}"
        else:
            return "La divisa no está en el diccionario."

    res = input("Introduce una divisa (Euro, Dollar, Yen): ")
    print(da_divisa(res))


def ej_2():
    '''Escribir un programa que pregunte al usuario su nombre,
    edad, dirección y teléfono y lo guarde en un diccionario.
    Después debe mostrar por pantalla el mensaje <nombre>
    tiene <edad> años, vive en <dirección> y su número de
    teléfono es <teléfono>.'''

    diccionario_personas = {}
    print("Buenos días, necesito que me introduzcas estos datos")
    nombre=input("Introduce tu nombre: ")
    edad=int(input("Introduce tu edad: "))
    direccion=input("Introduce tu dirección: ")
    telefono=input("Introduce tu teléfono: ")

    diccionario_personas[nombre]={"edad":edad,
                                  "direccion":direccion,
                                  "telefono":telefono}
    print(diccionario_personas[nombre])

def ej_3():
    '''Escribir un programa que guarde en un diccionario
    los precios de las frutas de la tabla, pregunte al
    usuario por una fruta, un número de kilos y muestre por
    pantalla el precio de ese número de kilos de fruta. Si
    la fruta no está en el diccionario debe mostrar un
    mensaje informando de ello.
    Fruta	Precio/KG
    Plátano	1.35
    Manzana	0.80
    Pera	0.85
    Naranja	0.70'''

    def devuelve_precio_fruta(fruta, kg):
        fruta = fruta.strip()
        fruta = fruta.capitalize()
        kg = float(kg)
        diccionario_frutas = {"Plátano":1.35,
                              "Manzana":0.80,
                              "Pera":0.85,
                              "Naranja":0.70}
        if fruta in diccionario_frutas:
            precio = diccionario_frutas[fruta] * kg
            return f"El precio de {kg} kg de {fruta} es {precio:.2f}€"
        else:
            return "La fruta no está en el diccionario."

    print("Bienvenido a la frutería")
    fruta=input("Introduce nombre de fruta: ")
    kg=input("Introduce cantidad de kilos: ")
    print(devuelve_precio_fruta(fruta, kg))

ej_1()
ej_2()
ej_3()
