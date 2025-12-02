print("EJERCICIOS UNIDAD 1")
while True:
    match input("1. Calcular la suma de dos números\n"
                "2. Calcular el área de un círculo\n"
                "3. Convertir grados Celsius a Fahrenheit\n"
                "4. Calcular el doble y el triple de un número\n"
                "5. Calcular la media de tres números\n"
                "6. Multiplicar dos números\n"
                "7. Concatenar dos cadenas de texto\n"
                "8. Mostrar un número repetido varias veces\n"
                "9. Calcular el área de un rectángulo\n"
                "10. Calcular el perímetro de un rectángulo\n"
                "11. Calcular salario semanal\n"
                "12. Decir nota sobre número\n"
                "Elige ejercicio (1-12 u otro para salir): "):

        case "1":
            print("")
            print("Calcular la suma de dos números")
            a = input("Introduce a: ")
            b = input("Introduce b: ")
            suma = int(a) + int(b)
            if suma > 100:
                print("La suma es mayor a 100, que pereza calcularla")
            elif suma < 0:
                print("La suma es menor a 0, para eso no sumes")
            else:
                print(f"La suma de a y b es: {suma}")
            print("")

        case "2":
            print("")
            print("Calcular el área de un círculo")
            pi = 3.14
            while True:
                try:
                    radio = float(input("Introduce el radio del círculo en cm: "))
                    area = (pi * radio ** 2).__round__(2)
                    if area >= 500:
                        print(f"El área del círculo es enorme: {area}cm^2")
                    else:
                        print(f"El área del círculo es: {area}cm^2")
                    break
                except:
                    print("El radio no es un número válido")
            print("")

        case "3":
            print("")
            print("Convertir grados Celsius a Fahrenheit")
            grados = int(input("Introduce los grados Celsius: "))
            fahrenheit = (grados * 9/5) + 32
            if grados >= 35:
                print("Vaya calor que hace...")
            print(f"Los grados Fahrenheit son: {fahrenheit}")
            print("")

        case "4":
            print("")
            print("Calcular el doble y el triple de un número")
            num = int(input("Introduce el nmúmero a duplicar y triplicar: "))
            doble = num*2
            triple = num*3
            print(f"El doble de {num} es: {doble}, y el triple de {num} es: {triple}")
            print("")

        case "5":
            print("")
            print("Calcular la media de tres números")
            num1 = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")
            num3 = input("Introduce el tercer número: ")
            media = ((float(num1) + float(num2) + float(num3)) / 3).__round__(2)
            esAprobado = media >= 5
            print(f"La media de {num1}, {num2} y {num3} es: {media}")
            if esAprobado:
                print("Has aprobado")
            else:
                print("No has aprobado")
            print("")

        case "6":
            print("")
            print("Multiplicar dos números")
            num1 = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")
            resultado = int(num1) * int(num2)
            print(f"El resultado de {num1} por {num2} es: {resultado}")
            print("")

        case "7":
            print("")
            print("Concatenar dos cadenas de texto")
            cad1 = input("Introduce la primera cadena de texto: ")
            cad2 = input("Introduce la segunda cadena de texto: ")
            resultado = cad1 + " " + cad2
            if len(resultado) > 72:
                print("La cadena resultante es muy larga, no se puede mostrar")
            else:
                print(resultado)
            print("")

        case "8":
            print("")
            print("Mostrar un número repetido varias veces")
            num = input("Introduce el número a repetir: ")
            if int(num)<0:
                print("El número es negativo, no lo muestro")
            else:
                for i in range(0,5):
                    print(num)
            print("")

        case "9":
            print("")
            print("Calcular el área de un rectángulo: ")
            base = input("Introduce la base en cm: ")
            altura = input("Introduce la altura en cm: ")
            area = (float(base) * float(altura)).__round__(2)
            print("El área del rectangulo es de: ", area, "cm^2")
            print("")

        case "10":
            print("")
            print("Calcular el perímetro de un rectángulo")
            base = input("Introduce la base en cm: ")
            altura = input("Introduce la altura en cm: ")
            perimetro = (float(base) * 2 + float(altura) * 2).__round__(2)
            print("El perímetro del rectangulo es de: ", perimetro, "cm")
            print("")

        case "11":
            print("")
            print("Calcular salario semanal")
            while True:
                try:
                    horas = int(input("Introduce la horas trabajadas en la semana: "))
                    if horas < 0:
                        raise ValueError
                        #raise ErrorDeDatos

                    rate = float(input("Introduce cuanto cobras por hora normal: "))
                    if rate < 0:
                        raise ValueError
                        #raise ErrorDeDatos

                    rate_extra = float(input("Introduce cuanto cobras por hora extra: "))
                    if rate_extra < 0:
                        raise ValueError
                        #raise ErrorDeDatos

                    if horas > 40:
                        euros = ((horas - 40) * rate_extra + 40 * rate).__round__(2)
                    else:
                        euros = (horas * rate).__round__(2)

                    print("Tu salario semanal es de: ", euros, "€")
                    break
                except:
                    print("No has introducido un número válido de horas")
            print("")
        case 12:
            print("")
            print("Decir nota sobre número")
            try:
                puntos = float(input("Introduce una puntuación entre 0.0 y 1.0: "))

                # Si el número está fuera de rango, lanzamos un error
                if puntos < 0.0 or puntos > 1.0:
                    raise ValueError("La puntuación debe estar entre 0.0 y 1.0")

                match puntos:
                    case p if p >= 0.9:
                        nota = "A"
                    case p if p >= 0.8:
                        nota = "B"
                    case p if p >= 0.7:
                        nota = "C"
                    case p if p >= 0.6:
                        nota = "D"
                    case _:
                        nota = "F"

                print("Tu calificación es:", nota)

            except ValueError as e:
                print("Error:", e)

        case _:
            print("")
            print("Salió del programa, ¡Gracias!")
            exit(0)

    input("Pulsa Enter...")
    print("")


    # esto serviría para que se pueda presionar
    # Enter para continuar (solo en windows, por eso no lo uso)
    # Si se pulsara otra tecla, no se tendría en cuenta

    # import msvcrt
    # print("Pulsa Enter para continuar...")
    # while True:
    #     tecla = msvcrt.getch()
    #     if tecla == b'\r':  # Código ASCII de Enter
    #         break

    class ErrorDeDatos(Exception):
        pass