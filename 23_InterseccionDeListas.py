'''
Dia 23 - Lista de duplicados.

Escribe una funcion para encontrar la interseccion de dos listas
'''

#SOLUCION: 

'''
Para resolver este desafio, se puede escribir una funcion
que identifique los elementos duplicados en ambas listas.
'''

def encontrar_interseccion(lista1, lista2):
    interseccion = list(set(lista1) & set(lista2))
    return interseccion

lista_a = [1,2,3,4,5,6]
lista_b = [5,6,7,8,9]

resultado = encontrar_interseccion(lista_a, lista_b)

print(f"La interseccion de las listas es: {resultado}")
