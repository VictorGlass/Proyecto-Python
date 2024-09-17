'''
Dia 21 - Lista Inversa.

1. Escribe una funcion para invertir una lista.
'''

#SOLUCION:
'''
El metodo reverse() modifica la lista directamente, 
pero de igual forma existen otras maneras de lograrlo.
'''

#*********************Usando reverse()
#Funcion para invertir la lista.
def invertir_lista(lista):
    lista.reverse()
    return lista

#Lista original 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Esta es la lista original: {lista}")

#Lista invertida
lista_invertida = invertir_lista(lista)
print(f"Esta es la lista invertida: {lista_invertida}")

#*********************Usando slicing()
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_invert = mi_lista[::-1]
print(f"Esta es la lista invertida usando el metodo slicing(): {lista_invert}")

#********************Usando reserved()
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_inv = list(reversed(lista_original))
print(f"Esta es la lista invertida usando reversed(): {lista_inv}")