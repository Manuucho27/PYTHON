import calculos as c
import funcModules as f
# from funcModules import saludar

while True:
    try:
        entrada=int(input("---- MENU ----"
                  "\n1. Area circulo"
                  "\n2. Area triangulo"
                  "\n3. Area cuadrado"
                  "\n4. Calcular precio entradas"
                  "\n5. Fibonacci (recursivo)"
                  "\n6. Salir"
                  "\nIntroduce tu opción: "))
        match entrada:
            case 1:
                print(f"Area circulo (normal): {c.area_circulo(3)}")
                print(f"Area circulo (pasando radio): {c.area_circulo(radio=4)}")
                print(f"Area circulo (sin pasar nada): {c.area_circulo()}")
                print("")
            case 2:
                print(f"Area triangulo (normal): {c.area_triangulo(3,4)}")
                print(f"Area triangulo (pasando base, altura): {c.area_triangulo(base=4, altura=5)}")
                print(f"Area triangulo (sin pasar nada): {c.area_triangulo()}")
                print("")
            case 3:
                print(f"Area cuadrado (normal): {c.area_cuadrado(4)}")
                print(f"Area cuadrado (pasando lado): {c.area_cuadrado(lado=5)}")
                print(f"Area cuadrado (sin pasar nada): {c.area_cuadrado()}")
                print("")
            case 4:
                print(f"El precio de la entrada (10€) para un menor y estudiante es: {f.precioEntradas(edad=15, estudiante=True)}")
                print(f"El precio de la entrada (10€) para un menor y no estudiante es: {f.precioEntradas(edad=15, estudiante=False)}")
                print(f"El precio de la entrada (10€) para un adulto y estudiante es: {f.precioEntradas(edad=18, estudiante=True)}")
                print(f"El precio de la entrada (10€) para un adulto y no estudiante es: {f.precioEntradas(edad=18, estudiante=False)}")
            case 5:
                print(f"Fibonacci (10): {f.fibonacci(10)}")
            case 6:
                break
    except ValueError as e:
        print("Error: ", e)
