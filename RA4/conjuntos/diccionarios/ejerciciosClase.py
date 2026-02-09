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
    print("Buenos días, necesito que me introduzcas estos datos.csv")
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

'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
donde <mes> es el nombre del mes.'''
def ej_4():

    def devuelve_fecha_string(fecha):
        fecha = fecha.split("/")
        meses = {
            "01": "Enero",
            "02": "Febrero",
            "03": "Marzo",
            "04": "Abril",
            "05": "Mayo",
            "06": "Junio",
            "07": "Julio",
            "08": "Agosto",
            "09": "Septiembre",
            "10": "Octubre",
            "11": "Noviembre",
            "12": "Diciembre"
        }
        mes= fecha[1]
        if len(mes)==1:
            mes="0"+mes
        return f"{fecha[0]} del {fecha[1]} del {fecha[2]} donde {meses[mes]} es el nombre del mes."

    fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
    print(devuelve_fecha_string(fecha))

'''Escribir un programa que almacene el diccionario con los créditos
de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5}
y después muestre por pantalla los créditos de cada asignatura en
el formato <asignatura> tiene <créditos> créditos, donde <asignatura>
es cada una de las asignaturas del curso, y <créditos> son sus créditos.
Al final debe mostrar también el número total de créditos del curso.'''

def ej_5():
    pass


'''Escribir un programa que cree un diccionario vacío y lo vaya llenado
con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se
añada un nuevo dato debe imprimirse el contenido del diccionario.'''

def ej_6():
    pass


'''Escribir un programa que cree un diccionario simulando una cesta
de la compra. El programa debe preguntar el artículo y su precio y
añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el
coste total, con el siguiente formato'''

def ej_7():
    cesta_diccionario = {}

    while True:
        print("Cesta de la compra")
        print("Contiene: ", cesta_diccionario)
        res=input("¿Quieres añadir un artículo a la cesta? Introduce 1: ")
        if res=="1":
            nombre=input("Introduce el nombre del artículo: ")
            precio=input("Introduce el precio del artícuo: ")
            cesta_diccionario[nombre]=int(precio)
            print("")
        else:
            print("Cesta finalizada")
            print(cesta_diccionario)
            print("Total a pagar: ", sum(cesta_diccionario.values()), "€")
            break


'''ej_1()
ej_2()
ej_3()
ej_4()
ej_5()
ej_6()
ej_7()'''

