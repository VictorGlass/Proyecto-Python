'''
Dia 30 - Ordena una lista.

Ordena una lista de numeros en orden ascendente.
'''

#SOLUCION:

'''
Para ordenar una lista de numeros en orden ascendente en Python,
podemos utilizar el metodo sort() que se aplicara directamente a las listas,
o a la funcion sorted() que devuelva una nueva lista ordenada sin modificar
la original.
'''

def ordenar_lista(numeros):
    numeros.sort() #Ordenara la lista
    return numeros

lista_numeros = [2, 5, 8, 1, 3, 6, 10, 4, 7, 9]
ordenada = ordenar_lista(lista_numeros)
print(f"Lista ordenada: {ordenada}")


#Forma de hacerlo sin modificar la lista:
def ordenar_lista_numeros(numeros):
    return sorted(numeros)

lista_num = [2, 7, 5, 8, 1, 3, 6, 10, 4, 9]
ordenar = ordenar_lista_numeros(lista_num)
print(f"Lista ordenada: {ordenar} vs Lista original: {lista_num}")

#De  esta forma se devuelve la misma lista pero ordenada sin alterar la original.