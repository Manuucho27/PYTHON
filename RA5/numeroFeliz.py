#Año feliz matemático
'''Un número feliz es un número definido por el siguiente proceso:
La suma repetitiva de los cuadrados de sus dígitos hasta que el número sea igual a 1'''
def es_numero_feliz(num):
    acumulador=0
    while acumulador != 1 and acumulador != 4:
        acumulador=0
        for digito in num:
            acumulador += int(digito)**2
        num=str(acumulador)
    return acumulador == 1

print(es_numero_feliz("2826"))
print(es_numero_feliz("2026"))
print(es_numero_feliz("2825"))