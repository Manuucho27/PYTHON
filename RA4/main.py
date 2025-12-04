import operacionString as av
import operacionSimpleString as simp

def mostrarMenu():
    print("\n========= MENÚ =========")
    print("1. Contar caracteres")
    print("2. Contar vocales")
    print("3. Contar letras")
    print("4. Contar números")
    print("5. Contar espacios")
    print("6. Contar signos de puntuación")
    print("7. Salir")
    print("========================")

def pedirTexto():
    while True:
        try:
            texto = input("Introduce una cadena de texto: ").strip()
            if not texto:  # Cadena vacía o solo espacios
                raise ValueError("La cadena está vacía")
            return texto
        except ValueError as e:
            print("Error: "+ e)


texto = pedirTexto()
while True:
    mostrarMenu()
    print("Recordamos que la cadena es: \""+texto+"\"")
    opcion = input("Selecciona una opción (1-7): ")

    match opcion:
        case "1":
            print("Caracteres:", av.contarCaracteres(texto))
        case "2":
            print("Vocales:", av.contarVocales(texto))
        case "3":
            print("Letras:", av.contarLetras(texto)) #Simple: simp.contarLetras(texto)
        case "4":
            print("Números:", av.contarNumeros(texto)) #Simple: simp.contarNumeros(texto)
        case "5":
            print("Espacios:", av.contarEspacios(texto)) #Simple: simp.contarEspacios(texto)
        case "6":
            print("Puntuación:", av.contarPuntos(texto)) #Simple: simp.contarPuntos(texto)
        case "7":
            print("Has cerrado el programa ¡Hasta luego!")
            break
        case _:
            print("Opción no válida, intenta de nuevo con un número del 1 al 7")

