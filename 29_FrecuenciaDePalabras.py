'''
Dia 29 - Frecuencia de palabras.

Crea un diccionario de palabras y sus frecuencias.
'''

#SOLUCION:

def frecuencia_palabras(oracion):
    #Es necesario convertir la oracion a minusculas y separar las palabras:
    palabras = oracion.lower().split()

    #Creamos un diccionario para almacenar las palabras:
    frecuencias = {}

    #Contamos la frecuencia de cada palabra:
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

#Ejemplo:
oracion = "El perro juega en el parque y el gato juega en casa"
resultado = frecuencia_palabras(oracion)
print(resultado)