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
    estadistica_base = 2.0

    caballero_dic = {
        'vida': estadistica_base * 2,
        'defensa': estadistica_base * 2,
        'ataque': estadistica_base,
        'alcance': estadistica_base
    }

    guerrero_dic = {
        'vida': caballero_dic['vida']/2,
        'defensa': caballero_dic['defensa']/2,
        'ataque': caballero_dic['ataque'] * 2,
        'alcance': caballero_dic['alcance'] * 2
    }

    arquero_dic = {
        'vida': guerrero_dic['vida'],
        'defensa': guerrero_dic['defensa'] / 2,
        'ataque': guerrero_dic['ataque'],
        'alcance': guerrero_dic['alcance'] * 2
    }

    return caballero_dic, guerrero_dic, arquero_dic

caballero, guerrero, arquero = configurar_personajes()
print("Propiedades del Caballero:", caballero)
print("Propiedades del Guerrero:", guerrero)
print("Propiedades del Arquero:", arquero)