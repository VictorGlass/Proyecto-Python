'''
Dia 28 - Palabras Inversas..

Invertir palabras de una oracion.
'''

#SOLUCION:

def invertir_palabras(oracion):
    #Separamos la oracion en palabras:
    palabras = oracion.split()
    #Invertimos las palabras usando reverse()
    palabras.reverse()
    #Unimos las palabras invertidas en una nueva oracion:
    oracion_invertida = ' '.join(palabras)
    return oracion_invertida

#Ejemplo de uso:
oracion = "Hoy es un gran dia"
print(invertir_palabras(oracion))