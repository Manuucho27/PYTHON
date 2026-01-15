def esAprobado(estudiante):
    return estudiante["nota"] >= 5

def esEstudiante(persona, lista_estudiantes):
    return persona in lista_estudiantes

def daNotas(id_estudiante):
    if id_estudiante not in daw2:
        return "No es estudiante de daw2"

    estudiante = daw2[id_estudiante]

    if esAprobado(estudiante):
        return "Aprobado con un " + str(estudiante["nota"])
    else:
        if estudiante["comportamiento"]:
            nota_suspenso = estudiante["nota"]
            estudiante["nota"] = 5
            return ("Era suspenso con un " + str(nota_suspenso) +
                    ", pero aprobó por buen comportamiento con un " + str(estudiante["nota"]))

    return "Suspenso con un " + str(estudiante["nota"])

daw2={
    "est1": {"nombre": "Ana", "nota": 7, "comportamiento": True},
    "est2": {"nombre": "Luis", "nota": 4, "comportamiento": False},
    "est3": {"nombre": "Marta", "nota": 9, "comportamiento": False},
    "est4": {"nombre": "Carlos", "nota": 5, "comportamiento": False},
    "est5": {"nombre": "Sofia", "nota": 3, "comportamiento": True},
    "est6": {"nombre": "Rafa", "nota": 10, "comportamiento": True},
    "est7": {"nombre": "Pedro", "nota": 2, "comportamiento": True},
    "est8": {"nombre": "Manu", "nota": 9, "comportamiento": True}
}

for id_estudiante, estudiante in daw2.items():
    print(f"{estudiante['nombre']}: {daNotas(id_estudiante)}")