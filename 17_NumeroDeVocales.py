'''
Dia 17 - Numero de vocales en una cadena.

1. Escribe una funcion para contar el numero de vocales de una cadena.
'''

#SOLUCION:

#Mensaje de bienvenida.
print("Juego de Vocales")
print("Bienvenido!")

#Declaracion de una variable para almacenar la cadena.
cadena = input("Ingresa una palabra: ")
#Funcion
def contar_vocales(cadena):
    #Variable vocales
    vocales = "aeiouAEIOU"
    #Contador iniciado en 0
    contador = 0
    #Bucle
    for vocal in cadena:
        if vocal in vocales:
            contador+=1
    return contador

print(f"La palabra es: {cadena} y tiene: {contar_vocales(cadena)} vocales.")


