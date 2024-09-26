'''
Dia 25 - Frecuencia de Palabras.

Escribe una funcion para contar la frecuencia de las palabras en una oracion.
'''

#SOLUCION:

def contar_frecuencua(oracion):
    #Se debe convertir la oracion a minusculas y separar en palabras
    palabras = oracion.lower().split()
    #Luego creamos un diccionario para almacenar la frecuencia de cada palabra.
    frecuencia = {}

    #Iteramos por cada palabra.
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

oracion = "Este es un ejemplo de la oracion ejemplo"
resultado = contar_frecuencua(oracion)
print(f"Frecuencia de palabras: {resultado}")