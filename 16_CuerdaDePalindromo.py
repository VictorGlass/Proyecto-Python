'''
Dia 16 - Cuerda de Palindromo.

1. Escribe una funcion para comprobar si una cadena dada es un palindromo.
'''

#SOLUCION:

'''
Palindromo: Es una palabra, frase, numero o cualquier secuencia de caracteres que se lee igual
            de adelante hacia atras que de atras hacia adelante, ignorando espacios, acentos o signos
            de puntuacion.

Por ejemplo: "ana"
             "reconocer"
             "Anita lava la tina"
'''

def es_palindromo(cadena):
    #Convertimos la cadena a minusculas y quitamos los espacios en blanco.
    cadena_limpia = cadena.replace(" ", "").lower()

    #Comprobamos si es igual a su reverso.
    return cadena_limpia == cadena_limpia[::-1]

#Ejemplo de uso.
cadena = input("Ingresa una cadena: ")
if es_palindromo(cadena):
    print(f"{cadena} es un palindromo.")
else:
    print(f"{cadena} no es un palindromo.")