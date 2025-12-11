# Menú interactivo para ejecutar los ejercicios
import sys
from pprint import pprint
from ejercicios import listar_ejercicios, demo_todos


def mostrar_menu(opciones):
    print('\n--- Menú de ejercicios ---')
    for k, (desc, _) in sorted(opciones.items(), key=lambda x: (x[0].isdigit(), x[0])):
        print(f"{k}. {desc}")
    print("q. Salir")



opciones = listar_ejercicios()
# modo demo no interactivo
if any(arg in ('--demo', '-d') for arg in sys.argv[1:]):
    print('Ejecutando demo no interactiva...')
    resultados = demo_todos()
    pprint(resultados)

# interactivo
try:
    while True:
        mostrar_menu(opciones)
        choice = input('Elige una opción: ').strip()
        if choice.lower() in ('q', 'quit', 'salir'):
            print('Saliendo...')
            break
        opt = opciones.get(choice)
        if not opt:
            print('Opción no válida. Intenta de nuevo.')
            continue
        desc, func = opt
        print(f'Ejecutando: {desc}\n')
        try:
            result = func()
            # mostrar resultado si la función devuelve algo y no ha impreso todo
            if result is not None:
                print('\nResultado devuelto:', result)
        except Exception as e:
            print('Error al ejecutar la función:', e)
except KeyboardInterrupt:
    print('\nInterrupción por teclado. Saliendo...')



