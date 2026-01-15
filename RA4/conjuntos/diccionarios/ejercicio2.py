'''TODO
    Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear
    cada clase de personaje jugable. Partiendo que la estadística base es 2,
    debes cumplir las siguientes condiciones:
        - El caballero tiene el doble de vida y defensa que un guerrero.
        - El guerrero tiene el doble de ataque y alcance que un caballero.
        - El arquero tiene la misma vida y ataque que un guerrero, pero
            la mitad de su defensa y el doble de su alcance.
        - Muestra como quedan las propiedades de los tres personajes.
'''
def configurar_personajes():
    estadistica_base = 2

    caballero = {
        'vida': estadistica_base * 2,
        'defensa': estadistica_base * 2,
        'ataque': estadistica_base,
        'alcance': estadistica_base
    }

    guerrero = {
        'vida': estadistica_base,
        'defensa': estadistica_base,
        'ataque': estadistica_base * 2,
        'alcance': estadistica_base * 2
    }

    arquero = {
        'vida': guerrero['vida'],
        'defensa': guerrero['defensa'] / 2,
        'ataque': guerrero['ataque'],
        'alcance': guerrero['alcance'] * 2
    }

    return caballero, guerrero, arquero

caballero, guerrero, arquero = configurar_personajes()
print("Propiedades del Caballero:", caballero)
print("Propiedades del Guerrero:", guerrero)
print("Propiedades del Arquero:", arquero)