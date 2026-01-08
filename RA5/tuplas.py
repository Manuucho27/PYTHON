#Crea una lista de strings con comandos funcionales. Ejemplo: "saludar"
def saludar(nombre):
    return f"Hola {nombre}"
def saludar_a_varios(*nombres):
    return f"Hola {', '.join(nombres)}"
def despedir(nombre):
    return f"Adios {nombre}"

lista = ("saluda", "saluda varios", "despide")
print(lista)
res=(input("Introduce una opción: ")).lower()
if lista.count(res)==1:
    match res:
        case "saluda":
            print(saludar("Juan"))
        case "saluda varios":
            print(saludar_a_varios("Juan", "Ana", "Luis"))
        case "despide":
            print(despedir("Juan"))
else:
    print("Comando no reconocido")