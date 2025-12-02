def calcular_salario_semanal(horas, rate, rate_extra):
    if horas > 40:
        euros = ((horas - 40) * rate_extra + 40 * rate).__round__(2)
    else:
        euros = (horas * rate).__round__(2)
    return euros

def calcularLetraNota(puntos=0):
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
    return nota

print("Calcular salario semanal")
while True:
    try:
        horas = int(input("Introduce la horas trabajadas en la semana: "))
        if horas < 0:
            raise ValueError

        rate = float(input("Introduce cuanto cobras por hora normal: "))
        if rate < 0:
            raise ValueError
        
        rate_extra = float(input("Introduce cuanto cobras por hora extra: "))
        if rate_extra < 0:
            raise ValueError

        print("Tu salario semanal es de: ", calcular_salario_semanal(horas, rate, rate_extra), "€")
        break
    except:
        print("No has introducido un número válido")

print("")
print("Decir nota sobre número")
try:
    puntos = float(input("Introduce una puntuación entre 0.0 y 1.0: "))

    if puntos < 0.0 or puntos > 1.0:
        raise ValueError("La puntuación debe estar entre 0.0 y 1.0")

    print("Tu calificación es:", calcularLetraNota(puntos))

except ValueError as e:
    print("Error:", e)