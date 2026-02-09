import random

print("EJERCICIOS UNIDAD 2 - BUCLES Y EXCEPCIONES")

import random

def bloque1():
    while True:
        opcion = input(
            "\n=== BLOQUE 1 ===\n"
            "1. Calculadora básica\n"
            "2. Tabla de multiplicar\n"
            "3. Adivina el número\n"
            "4. Comprobar si un número es primo\n"
            "5. Números primos hasta N\n"
            "6. Análisis de notas.csv de alumnos\n"
            "0. Volver al menú principal\n"
            "Elige ejercicio (0-6): "
        )

        match opcion:
            case "1":
                print("\nCalculadora de operaciones básicas")
                while True:
                    try:
                        op = input("Introduce la operación (+, -, *, / o 'salir'): ")
                        if op.lower() == "salir":
                            break
                        num1 = float(input("Introduce el primer número: "))
                        num2 = float(input("Introduce el segundo número: "))
                        if op == "+":
                            print(f"Resultado: {num1 + num2}")
                        elif op == "-":
                            print(f"Resultado: {num1 - num2}")
                        elif op == "*":
                            print(f"Resultado: {num1 * num2}")
                        elif op == "/":
                            if num2 == 0:
                                raise ZeroDivisionError("No se puede dividir entre cero.")
                            print(f"Resultado: {num1 / num2}")
                        else:
                            raise ValueError("Operación no reconocida.")
                    except ValueError as e:
                        print("Error de valor:", e)
                    except ZeroDivisionError as e:
                        print("Error matemático:", e)
                    print("")

            case "2":
                print("\nTabla de multiplicar")
                try:
                    n = int(input("Introduce un número entero: "))
                    print(f"Tabla de multiplicar del {n}:")
                    for i in range(1, 11):
                        print(f"{n} x {i} = {n * i}")
                except ValueError:
                    print("Error: Debes introducir un número entero válido.")
                print("")

            case "3":
                print("\nJuego: Adivina el número")
                numeroSecreto = random.randint(1, 100)
                while True:
                    try:
                        intento = int(input("Adivina el número (1-100): "))
                        if intento < numeroSecreto:
                            print("Demasiado bajo.")
                        elif intento > numeroSecreto:
                            print("Demasiado alto.")
                        else:
                            print("¡Correcto! Has adivinado el número.")
                            break
                    except ValueError:
                        print("Error: Introduce un número entero.")
                print("")

            case "4":
                print("\nComprobar si un número es primo")
                try:
                    n = int(input("Introduce un número entero positivo: "))
                    if n <= 0:
                        raise ValueError("Debe ser un número positivo.")
                    if n == 1:
                        print("1 no es primo por definición.")
                    else:
                        i = 2
                        es_primo = True
                        while i * i <= n:
                            if n % i == 0:
                                es_primo = False
                                break
                            i += 1
                        if es_primo:
                            print(f"{n} es un número primo.")
                        else:
                            print(f"{n} no es primo.")
                except ValueError as e:
                    print("Error:", e)
                print("")

            case "5":
                print("\nNúmeros primos hasta N")
                try:
                    N = int(input("Introduce un número entero positivo: "))
                    if N < 2:
                        raise ValueError("Debe ser mayor o igual a 2.")
                    for num in range(2, N + 1):
                        es_primo = True
                        i = 2
                        while i * i <= num:
                            if num % i == 0:
                                es_primo = False
                                break
                            i += 1
                        if es_primo:
                            print(num, end=" ")
                    print("")
                except ValueError as e:
                    print("Error:", e)
                print("")

            case "6":
                print("\nAnálisis de notas.csv de alumnos")

                notas = []
                while True:
                    entrada = input("Introduce una nota (0-10) o 'fin' para terminar: ")
                    if entrada.lower() == "fin":
                        break
                    try:
                        nota = float(entrada)
                        if nota < 0 or nota > 10:
                            raise ValueError("La nota debe estar entre 0 y 10.")
                        notas.append(nota)
                    except ValueError as e:
                        print("Error:", e)

                if not notas:
                    print("No se introdujeron notas.csv.")
                else:
                    aprobados = sum(1 for n in notas if n >= 5)
                    media = sum(notas) / len(notas)
                    print(f"\nTotal de alumnos: {len(notas)}")
                    print(f"Aprobados: {aprobados}")
                    print(f"Nota media: {media:.2f}")
                    print(f"Nota más alta: {max(notas)}")
                    print(f"Nota más baja: {min(notas)}")
                print("")

            case "0":
                print("Volviendo al menú principal...\n")
                break

            case _:
                print("Opción no válida, intenta de nuevo.")


def bloque2():
    while True:
        opcion = input(
            "\n=== BLOQUE 2 ===\n"
            "1. Control de inventario.csv inteligente\n"
            "2. Control de inventario.csv simple\n"
            "3. Inversión de dinero\n"
            "4. Menú de restaurante\n"
            "5. Cuenta atrás\n"
            "0. Volver al menú principal\n"
            "Elige ejercicio (0-6): "
        )

        match opcion:
            case "1":
                print("\nControl de inventario.csv inteligente")

                inventario = {}

                while True:
                    print("\n--- MENÚ INVENTARIO ---")
                    print("1. Añadir producto")
                    print("2. Vender producto")
                    print("3. Mostrar inventario.csv")
                    print("4. Eliminar producto")
                    print("5. Salir al menú principal")

                    opcion = input("Elige una opción: ")

                    match opcion:
                        case "1":
                            nombre = input("Nombre del producto: ").strip().capitalize()
                            try:
                                cantidad = int(input("Cantidad a añadir: "))
                                if cantidad <= 0:
                                    raise ValueError("La cantidad debe ser positiva.")
                                inventario[nombre] = inventario.get(nombre, 0) + cantidad
                                print(f"Producto '{nombre}' añadido correctamente ({cantidad} unidades).")
                            except ValueError as e:
                                print("Error:", e)

                        case "2":
                            nombre = input("Nombre del producto a vender: ").strip().capitalize()
                            if nombre not in inventario:
                                print("Ese producto no existe en el inventario.csv.")
                                continue
                            try:
                                cantidad = int(input("Cantidad a vender: "))
                                if cantidad <= 0:
                                    raise ValueError("La cantidad debe ser positiva.")
                                if cantidad > inventario[nombre]:
                                    raise ValueError("No hay suficiente stock para realizar la venta.")
                                inventario[nombre] -= cantidad
                                if inventario[nombre] == 0:
                                    print(f"Se agotaron las existencias de '{nombre}'.")
                                else:
                                    print(f"Venta realizada. Quedan {inventario[nombre]} unidades de '{nombre}'.")
                            except ValueError as e:
                                print("Error:", e)

                        case "3":
                            if not inventario:
                                print("El inventario.csv está vacío.")
                            else:
                                print("\nInventario actual:")
                                for prod, cant in inventario.items():
                                    print(f"- {prod}: {cant}")

                        case "4":
                            nombre = input("Nombre del producto a eliminar: ").strip().capitalize()
                            if nombre in inventario:
                                confirmar = input(f"¿Seguro que deseas eliminar '{nombre}'? (s/n): ").lower()
                                if confirmar == "s":
                                    del inventario[nombre]
                                    print(f"Producto '{nombre}' eliminado correctamente.")
                                else:
                                    print("Operación cancelada.")
                            else:
                                print("Ese producto no existe en el inventario.csv.")

                        case "5":
                            print("Volviendo al menú del bloque...")
                            break

                        case _:
                            print("Opción no válida, intenta de nuevo.")

            case "2":
                print("\nControl de inventario.csv simple (Manzanas, Plátanos y Peras)")
                manzanas = platanos = peras = 0

                while True:
                    print("\n--- MENÚ INVENTARIO ---")
                    print("1. Añadir stock")
                    print("2. Vender producto")
                    print("3. Mostrar inventario.csv")
                    print("4. Volver al menú del bloque")

                    opcion = input("Elige una opción: ")

                    match opcion:
                        case "1":
                            print("\nProductos disponibles: Manzanas, Plátanos, Peras")
                            producto = input("¿Qué producto quieres añadir?: ").strip().lower()
                            try:
                                cantidad = int(input("Cantidad a añadir: "))
                                if cantidad <= 0:
                                    raise ValueError("La cantidad debe ser positiva.")
                                if producto == "manzanas":
                                    manzanas += cantidad
                                elif producto in ["plátanos", "platanos"]:
                                    platanos += cantidad
                                elif producto == "peras":
                                    peras += cantidad
                                else:
                                    print("Producto no válido.")
                                    continue
                                print(f"Se añadieron {cantidad} unidades de {producto}.")
                            except ValueError as e:
                                print("Error:", e)

                        case "2":
                            print("\nProductos disponibles: Manzanas, Plátanos, Peras")
                            producto = input("¿Qué producto quieres vender?: ").strip().lower()
                            try:
                                cantidad = int(input("Cantidad a vender: "))
                                if cantidad <= 0:
                                    raise ValueError("La cantidad debe ser positiva.")
                                if producto == "manzanas":
                                    if cantidad > manzanas:
                                        raise ValueError("No hay suficientes manzanas.")
                                    manzanas -= cantidad
                                elif producto in ["plátanos", "platanos"]:
                                    if cantidad > platanos:
                                        raise ValueError("No hay suficientes plátanos.")
                                    platanos -= cantidad
                                elif producto == "peras":
                                    if cantidad > peras:
                                        raise ValueError("No hay suficientes peras.")
                                    peras -= cantidad
                                else:
                                    print("Producto no válido.")
                                    continue
                                print(f"Venta realizada: {cantidad} {producto}.")
                            except ValueError as e:
                                print("Error:", e)

                        case "3":
                            print("\nINVENTARIO ACTUAL:")
                            print(f"- Manzanas: {manzanas}")
                            print(f"- Plátanos: {platanos}")
                            print(f"- Peras: {peras}")

                        case "4":
                            print("Volviendo al menú del bloque...")
                            break

                        case _:
                            print("Opción no válida, intenta de nuevo.")

            case "3":
                print("\nInversión de dinero por años")
                try:
                    dineroEnBanco = float(input("Introduce la cantidad de dinero a ingresar (en €): "))
                    if dineroEnBanco <= 0:
                        raise ValueError("La cantidad de dinero debe ser positiva.")
                    interesAnual = float(input("Introduce el interés anual (en %): "))
                    if interesAnual < 0 or interesAnual > 100:
                        raise ValueError("El porcentaje debe estar entre 0 y 100.")
                    interes = interesAnual / 100
                    anios = int(input("Introduce los años de inversión: "))
                    if anios <= 0:
                        raise ValueError("Los años deben ser positivos.")

                    for _ in range(anios):
                        dineroEnBanco += dineroEnBanco * interes
                    print(f"\nEl dinero final será: {dineroEnBanco:.2f}€ tras {anios} años con"
                          f"{interesAnual}% de interés anual.")
                except ValueError as e:
                    print("Error:", e)

            case "4":
                print("\nMenú de restaurante")
                plato = {1: "Macarrones", 2: "Sushi", 3: "Filete de pollo"}
                bebida = {1: "Fanta", 2: "Coca-Cola", 3: "Cerveza"}
                complemento = {1: "Nuggets", 2: "Gyozas", 3: "Mini pizza"}
                precioPlato = {"Macarrones": 6, "Sushi": 10, "Filete de pollo": 5}
                precioBebida = {"Fanta": 1.5, "Coca-Cola": 2, "Cerveza": 1.2}
                precioComplemento = {"Nuggets": 1.5, "Gyozas": 2, "Mini pizza": 3}
                pago = {1: "Tarjeta", 2: "Efectivo", 3: "Transferencia"}

                try:
                    print("\n--- COMIDAS ---")
                    comida = plato[int(input("1. Macarrones\n2. Sushi\n3. Filete de pollo\nElige: "))]
                    print("\n--- BEBIDAS ---")
                    bebidaSel = bebida[int(input("1. Fanta\n2. Coca-Cola\n3. Cerveza\nElige: "))]
                    print("\n--- COMPLEMENTOS ---")
                    comp = complemento[int(input("1. Nuggets\n2. Gyozas\n3. Mini pizza\nElige: "))]

                    total = precioPlato[comida] + precioBebida[bebidaSel] + precioComplemento[comp]
                    print(f"\nTu pedido:\n{comida}, {bebidaSel}, {comp}\nTotal: {total:.2f}€")

                    pagoSel = pago[int(input("\nMétodo de pago:\n1. Tarjeta\n2. Efectivo\n3. Transferencia\nElige: "))]
                    print(f"Pago con {pagoSel}. ¡Gracias por su compra!")

                except (ValueError, KeyError):
                    print("Error: opción no válida.")

            case "5":
                print("\nCuenta atrás")
                try:
                    num = int(input("Introduce un número entero positivo: "))
                    for i in range(num, -1, -1):
                        print(i, end=", " if i != 0 else "\n")
                except ValueError as e:
                    print("Error:", e)

            case "6":
                print("\nMúltiplos de 7")
                for num in range(81, 200):
                    if num % 7 != 0:
                        continue  # saltar los que no son múltiplos de 7
                    print(f"El primer múltiplo de 7 mayor que 80 y menor que 200 es: {num}")
                    break

            case "0":
                print("Volviendo al menú principal...\n")
                break

            case _:
                print("Opción no válida, intenta de nuevo.")


# --- MENÚ PRINCIPAL ---
while True:
    opcion = input(
        "\n=== MENÚ PRINCIPAL ===\n"
        "1. Bloque 1 (Ejercicios 1 al 6)\n"
        "2. Bloque 2 (Ejercicios 7 al 11)\n"
        "0. Salir\n"
        "Elige una opción (0-2): "
    )

    match opcion:
        case "1":
            bloque1()
        case "2":
            bloque2()
        case "0":
            print("\nSaliendo del programa, ¡gracias!")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")
