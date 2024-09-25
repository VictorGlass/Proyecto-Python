'''
Dia 24 - De las palabras a la oracion.

Escribe una funcion para convertir una lista de palabras en una oracion.
'''

#SOLUCION:

def palabras_a_oracion(lista_palabras):
    #Se unen las palabras con un espacio para formar la oracion.
    oracion = ' '.join(lista_palabras)
    return oracion

palabras = ["Hola", "esta", "es", "una", "oracion"]
resultado = palabras_a_oracion(palabras)

print(f"Oracion sin unir las palabras: {palabras}")
print(f"Oracion con palabras unidas: {resultado}")