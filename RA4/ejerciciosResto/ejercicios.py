# Ejercicios de cadenas - implementaciones

VOWELS = set("aeiouáéíóúAEIOUÁÉÍÓÚ")

# Ejercicio 1 (Sebastian Becerra)
def ejercicio_1_demo():
    original = " este ejercicio es muy complicado "
    # buscar índice de la palabra 'complicado' en la cadena original (sin espacios iniciales)
    idx = original.strip().find("complicado")
    # sustituir "complicado" por "facilísimo"
    mod = original.strip().replace("complicado", "facilísimo")
    # cada palabra comienza en mayúscula y sin espacios
    words = [w.capitalize() for w in mod.split()]
    joined = "".join(words)
    inverted = joined[::-1]
    return {
        "original": original,
        "index_complicado": idx,
        "modified_joined": joined,
        "inverted": inverted,
    }

# Ejercicio 2 (Ana López)
def ejercicio_2_process(s: str) -> str:
    # pasar a minúsculas y eliminar espacios
    s2 = s.lower().replace(" ", "")
    # letras en posiciones pares (contando desde 1) las cambiamos por asteriscos
    result_chars = []
    for i, ch in enumerate(s2, start=1):
        if ch.isalpha() and i % 2 == 0:
            result_chars.append("*")
        else:
            result_chars.append(ch)
    return "".join(result_chars)

# Ejercicio 3 (Clasificador de palabras)
def clasificar_palabras(texto: str) -> dict:
    palabras = texto.split()
    res = {"empiezan_por_vocal": [], "terminan_consonante": [], "contienen_numero": []}
    for w in palabras:
        # limpiar signos alrededor
        w_clean = w.strip(".,;:!?()[]{}\"'\n")
        if not w_clean:
            continue
        # contiene numero
        if any(ch.isdigit() for ch in w_clean):
            res["contienen_numero"].append(w_clean)
        # empieza por vocal
        if w_clean[0].lower() in "aeiouáéíóú":
            res["empiezan_por_vocal"].append(w_clean)
        # termina en consonante
        last = w_clean[-1].lower()
        if last.isalpha() and last not in "aeiouáéíóú":
            res["terminan_consonante"].append(w_clean)
    return res

# Ejercicio 4 (comprobar si todos los caracteres son mayúsculas)
def es_todo_mayusculas(s: str) -> bool:
    # devolver True si no hay ninguna letra minúscula
    return all(not ch.islower() for ch in s)

# Ejercicio 5 (longitud, minúsculas, ultimas 5)
def procesar_cadena_info(s: str):
    longitud = len(s)
    minus = s.lower()
    ultimas5 = s[-5:] if len(s) >= 5 else s
    return longitud, minus, ultimas5

# Ejercicio 6 (validar email con 3 intentos) - función de validación y versión no interactiva
def validar_email(email: str) -> bool:
    e = email.strip()
    if "@" not in e:
        return False
    if not (e.lower().endswith('.com') or e.lower().endswith('.es')):
        return False
    # comprobación simple adicional: algo@algo.dominio
    parts = e.split('@')
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return False
    return True

def pedir_email_con_intentos(max_intentos: int = 3):
    intentos = 0
    while intentos < max_intentos:
        email = input('Introduce un email: ').strip()
        if validar_email(email):
            print('Email válido:', email)
            return email
        else:
            intentos += 1
            print(f'Email no válido. Te quedan {max_intentos - intentos} intentos.')
    print('Se han agotado los intentos.')
    return None

# Ejercicio 8 (varias transformaciones)
def procesar_frase(frase: str, palabra_a_contar: str = None) -> dict:
    stripped = frase.strip()
    lower = stripped.lower()
    upper = stripped.upper()
    capitalized = stripped.capitalize()
    replaced = stripped.replace(',', '.')
    count_word = 0
    if palabra_a_contar is not None:
        # cuenta ignorando mayúsc/minúsc
        count_word = lower.count(palabra_a_contar.lower())
    empieza_vocal = stripped[:1].lower() in 'aeiouáéíóú' if stripped else False
    num_palabras = len(stripped.split()) if stripped else 0
    return {
        'stripped': stripped,
        'lower': lower,
        'upper': upper,
        'capitalized': capitalized,
        'replaced_commas': replaced,
        'count_word': count_word,
        'starts_with_vowel': empieza_vocal,
        'num_words': num_palabras,
    }

# Ejercicio 9 (Volviendo a Messenger)
def ejercicio_9_procesar(frase: str) -> str:
    palabras = frase.split()
    n = len(palabras)
    if n == 0:
        return frase
    if n % 2 == 0:
        # convertir letras pares a mayúsculas y las impares a minúsculas
        # contaremos posiciones de caracteres empezando en 1, incluyendo espacios y signos
        result_chars = []
        for i, ch in enumerate(frase, start=1):
            if ch.isalpha():
                if i % 2 == 0:
                    result_chars.append(ch.upper())
                else:
                    result_chars.append(ch.lower())
            else:
                result_chars.append(ch)
        return ''.join(result_chars)
    else:
        # devolver frase con palabras en orden invertido
        return ' '.join(reversed(palabras))

# Ejercicio 10 (contar vocales y combinar reemplazando posiciones impares por 'C')
def contar_vocales(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in 'aeiou')

def ejercicio_10_procesar(a: str, b: str):
    suma_vocales = contar_vocales(a) + contar_vocales(b)
    combinada = a + b
    result_chars = []
    for i, ch in enumerate(combinada, start=1):
        if i % 2 == 1:
            result_chars.append('C')
        else:
            result_chars.append(ch)
    reemplazada = ''.join(result_chars)
    return suma_vocales, reemplazada

# Ejercicio 11 (validar DNI)
DNI_LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def validar_dni(dni: str) -> bool:
    d = dni.strip().upper()
    # permitir formatos con espacio o guion
    d = d.replace(' ', '').replace('-', '')
    if len(d) != 9:
        return False
    num = d[:8]
    letra = d[8]
    if not num.isdigit() or not letra.isalpha():
        return False
    index = int(num) % 23
    return DNI_LETRAS[index] == letra

# Ejercicio 12 (contar letras, numeros y espacios)
def contar_letras_numeros_espacios(s: str) -> str:
    letras = sum(1 for ch in s if ch.isalpha())
    numeros = sum(1 for ch in s if ch.isdigit())
    espacios = sum(1 for ch in s if ch == ' ')
    return f"tienes {letras} letras, {numeros} numeros y {espacios} espacios"

# Funciones de demo rápida para mostrar resultados sin interacción
def demo_todos():
    demos = {}
    demos['ej1'] = ejercicio_1_demo()
    demos['ej2'] = ejercicio_2_process("Esto Es Un Ejemplo 123")
    demos['ej3'] = clasificar_palabras("Esto es 1 prueba y otra, acabando en s y palabra3")
    demos['ej4_true'] = es_todo_mayusculas("ABC123!?")
    demos['ej4_false'] = es_todo_mayusculas("AbC")
    demos['ej5'] = procesar_cadena_info("Hola Mundo")
    demos['ej6_valid'] = validar_email("usuario@dominio.com")
    demos['ej6_invalid'] = validar_email("bademail@x")
    demos['ej8'] = procesar_frase("  Hola, mundo, esto es una prueba, prueba  ", "prueba")
    demos['ej9_even'] = ejercicio_9_procesar("Estoy estudiando Python y no quiero suspender")
    demos['ej10'] = ejercicio_10_procesar("hola", "mundo")
    demos['ej11_good'] = validar_dni("12345678Z")
    demos['ej11_examples'] = ["12345678Z", "00000000T", "87654321A"]
    demos['ej12'] = contar_letras_numeros_espacios("Tengo 2 manzanas y 10 naranjas")
    return demos

# ----- Wrappers estilo "como sueles programar" -----
# A continuación agrego funciones `ej1`..`ej12` (omite 7) que piden entrada si es necesario,
# imprimen el resultado y lo devuelven. Mantengo las funciones originales para reutilizar la lógica.

def ej1():
    """Ejercicio 1: transformar la cadena y mostrar resultados."""
    res = ejercicio_1_demo()
    print("Original:", res['original'])
    print("Índice de 'complicado':", res['index_complicado'])
    print("Modificada (sin espacios, cada palabra capitalizada):", res['modified_joined'])
    print("Invertida:", res['inverted'])
    return res


def ej2(s: str = None):
    """Ejercicio 2: si no se proporciona s, se pide por teclado."""
    if s is None:
        s = input('Introduce una cadena para procesar (ej2): ')
    salida = ejercicio_2_process(s)
    print('Resultado:', salida)
    return salida


def ej3(texto: str = None):
    if texto is None:
        texto = input('Introduce un texto para clasificar palabras (ej3): ')
    res = clasificar_palabras(texto)
    print('Clasificación:')
    for k, lst in res.items():
        print(f" - {k} ({len(lst)}): {lst}")
    return res


def ej4(s: str = None):
    if s is None:
        s = input('Introduce una cadena para comprobar mayúsculas (ej4): ')
    ok = es_todo_mayusculas(s)
    print('¿Todos los caracteres están en mayúsculas (ninguna minúscula)?', ok)
    return ok


def ej5(s: str = None):
    if s is None:
        s = input('Introduce una cadena para procesar (ej5): ')
    longitud, minus, ultimas5 = procesar_cadena_info(s)
    print(f'Longitud: {longitud}, minúsculas: {minus}, últimas 5: {ultimas5}')
    return longitud, minus, ultimas5


def ej6():
    """Ejercicio 6: usar la función interactiva con 3 intentos."""
    print('Validación de email (tienes 3 intentos):')
    return pedir_email_con_intentos()


def ej8():
    frase = input('Introduce una frase (ej8): ')
    palabra = input('Introduce la palabra a contar (dejar vacío para 0): ')
    palabra = palabra if palabra.strip() else None
    res = procesar_frase(frase, palabra)
    print('Resultados:')
    for k, v in res.items():
        print(f' - {k}: {v}')
    return res


def ej9():
    frase = input('Introduce una frase para el ejercicio 9: ')
    res = ejercicio_9_procesar(frase)
    print('Resultado:', res)
    return res


def ej10():
    a = input('Cadena A (ej10): ')
    b = input('Cadena B (ej10): ')
    suma_vocales, reemplazada = ejercicio_10_procesar(a, b)
    print(f'Suma vocales: {suma_vocales}, combinada reemplazada: {reemplazada}')
    return suma_vocales, reemplazada


def ej11():
    dni = input('Introduce un DNI para validar (ej11, formato 12345678Z): ')
    ok = validar_dni(dni)
    print('DNI válido:' if ok else 'DNI no válido:', ok)
    return ok


def ej12():
    s = input('Introduce una cadena para contar letras/números/espacios (ej12): ')
    res = contar_letras_numeros_espacios(s)
    print(res)
    return res


def listar_ejercicios():
    return {
        '1': ('Ejercicio 1', ej1),
        '2': ('Ejercicio 2', ej2),
        '3': ('Ejercicio 3', ej3),
        # 4
        '4': ('Ejercicio 4', ej4),
        '5': ('Ejercicio 5', ej5),
        '6': ('Ejercicio 6', ej6),
        # 7 omitido
        '8': ('Ejercicio 8', ej8),
        '9': ('Ejercicio 9', ej9),
        '10': ('Ejercicio 10', ej10),
        '11': ('Ejercicio 11', ej11),
        '12': ('Ejercicio 12', ej12),
        'd': ('Demo (no interactiva)', demo_todos),
    }
