print("EJERCICIOS UNIDAD 2 - EXCEPCIONES")
while True:
    match input("1. Verificación de número primo\n"
                "2. Conversor de divisas\n"
                "3. Cálculo de raíces reales\n"
                "4. Simulador de cajero automático\n"
                "5. Calculadora de operaciones\n"
                "Elige ejercicio (1-5 u otra tecla para salir): "):

        case "1":
            print("\nVerificación de número primo con control de errores")
            try:
                n = int(input("Introduce un número entero positivo: "))
                if n <= 0:
                    raise ValueError("El número debe ser positivo.")
                if n == 1:
                    print("1 no es primo por definición.")
                else:
                    es_primo = True
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0:
                            print(f"No es primo porque es divisible por {i}.")
                            es_primo = False
                            break
                    if es_primo:
                        print(f"{n} es un número primo.")
            except ValueError as e:
                print("Error:", e)
            print("")

        case "2":
            print("\nConversor de divisas con control de errores")
            tasas = {"USD": 1.08, "GBP": 0.86, "JPY": 157.3}
            try:
                euros = float(input("Introduce la cantidad en euros: "))
                if euros <= 0:
                    raise ValueError("La cantidad debe ser positiva.")
                divisa = input("Introduce la divisa destino (USD, GBP o JPY): ").upper()
                if divisa not in tasas:
                    raise ValueError("Divisa no reconocida.")
                convertido = euros * tasas[divisa]
                print(f"{euros}€ equivalen a {convertido:.2f} {divisa}")
            except ValueError as e:
                print("Error:", e)
            print("")

        case "3":
            print("\nCálculo de raíces reales de una ecuación cuadrática")
            try:
                a = float(input("Introduce a: "))
                if a == 0:
                    raise ValueError("a no puede ser 0, no sería una ecuación cuadrática.")
                b = float(input("Introduce b: "))
                c = float(input("Introduce c: "))
                D = b**2 - 4*a*c
                if D < 0:
                    raise ValueError("No existen raíces reales (discriminante negativo).")
                x1 = (-b + D**0.5) / (2*a)
                x2 = (-b - D**0.5) / (2*a)
                print(f"Las raíces reales son: x1 = {x1:.2f}, x2 = {x2:.2f}")
            except ValueError as e:
                print("Error:", e)
            print("")

        case "4":
            print("\nSimulador de cajero automático")
            try:
                saldo = float(input("Introduce el saldo inicial: "))
                retiro = float(input("Introduce la cantidad a retirar: "))
                if saldo < 0 or retiro < 0:
                    raise ValueError("Los valores deben ser positivos.")
                if retiro > saldo:
                    raise ValueError("Saldo insuficiente para retirar esa cantidad.")
                saldo -= retiro
                print(f"Retiro exitoso. Saldo restante: {saldo:.2f}€")
            except ValueError as e:
                print("Error:", e)
            print("")

        case "5":
            print("\nCalculadora de operaciones con manejo múltiple de excepciones")
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                op = input("Introduce la operación (+, -, *, /): ")
                if op == "+":
                    resultado = num1 + num2
                elif op == "-":
                    resultado = num1 - num2
                elif op == "*":
                    resultado = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        raise ZeroDivisionError("No se puede dividir entre cero.")
                    resultado = num1 / num2
                else:
                    raise ValueError("Operación no reconocida.")
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print("Error de valor:", e)
            except ZeroDivisionError as e:
                print("Error matemático:", e)
            except Exception as e:
                print("Error desconocido:", e)
            print("")

        case _:
            print("\nSalió del programa, ¡Gracias!")
            exit(0)

    input("Pulsa Enter para continuar...")
    print("")
