'''
Dia 27 - Palabra mas larga.

encuentra la palabra mas larga de una oracion.
'''

#SOLUCION:

def palabra_mas_larga(oracion):
    #Se debe dividir la oracion en palabras:
    palabras = oracion.split()

    #Usare la funcion max con la longitud de las palabras como criterio:
    palabra_larga = max(palabras, key=len)

    return palabra_larga

print(palabra_mas_larga("Encontremos la palabra mas larga de la oracion"))
print(palabra_mas_larga("Hoy es un dia esplendido"))
