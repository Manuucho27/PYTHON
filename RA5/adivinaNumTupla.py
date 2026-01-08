#Adivina en que posición está el número n (aleatorio 1-10) en una tupla (usa el metodo index())
import random

def isNumCorrecto(num_indice, num_final, tupla):
    if num_indice == tupla.index(num_final):
        return True
    return False

print("Dado este número en una tupla, adivina su posición:")
tupla= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num = random.randint(1, 10)
while True:
    print("El número es", num)
    res=int(input("Introduce la posición en la que crees que está (0-9): "))
    if isNumCorrecto(res, num, tupla):
        print("Has acertado!")
        break
    else:
        if res<0 or res>9:
            print ("El número tiene que estar entre 0 y 9")
        else:
            if res<tupla.index(num):
                print("El indice es mayor del que has introducido")
            else:
                print("El indice es menor del que has introducido")
        print("Has fallado! Inténtalo de nuevo")
        print("")