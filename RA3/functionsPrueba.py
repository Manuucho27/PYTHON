import random

def calcular_total_compra(*precios, iva, descuento=0):
    subtotal = sum(precios)
    subtotal = subtotal * (1 - descuento / 100)
    subtotal = subtotal + subtotal * iva / 100
    return subtotal

def sorteo_multiple(*participantes, mensaje=None, premio=500):
    if mensaje is not None:
        return f"{mensaje}: {random.choice(participantes)} ha ganado {premio}"
    else:
        return f"{random.choice(participantes)} ha ganado {premio}"