'''
Dia 26 - Cuerda de anagramas.

Escriba una funcion para comprobar si dos cadenas son anagramas.
'''

#SOLUCION:

def son_anagramas(cadena1, cadena2):
    #Primero eliminamos espacios y convertir las cadenas a minusculas.
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()

    #Luego hay que comparar las cadenas.
    return sorted(cadena1) == sorted(cadena2)

print(son_anagramas("amor", "roma"))
print(son_anagramas("hola", "aloh"))
