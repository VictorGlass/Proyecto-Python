'''
Dia 14 - Año Bisiesto.

1. Escribir un programa que compruebe si un año de entrada determinado es bisiesto o no.
'''

print("Bienvenido! ingresa un año y te dire si es bisiesto o no")
usuario_anio = int(input("Ingrese un año: "))

def anio_bisiesto(usuario_anio):
    if usuario_anio % 4 == 0 and (usuario_anio % 100 != 0 or usuario_anio % 400 == 0):
        return "El año es bisiesto"
    else:
        "No es bisiesto"

print(anio_bisiesto(usuario_anio))