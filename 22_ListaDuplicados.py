'''
Dia 22 - Lista de duplicados.

Escribe una funcion para eliminar duplicados de una lista.
'''

#SOLUCION:

'''
Se podrian utilizar 2 metodos.
'''
#Usando set.
def eliminar_duplicados(lista):
    return list(set(lista))

lista = [1, 2, 2, 3, 1, 4, 5, 5]
lista_sin_duplicados = eliminar_duplicados(lista)
print(f"Lista con duplucados: {lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

#Preservando el orden.

def eliminar_los_duplicados(lista):
    lista_s_duplicados = []
    for elemento in lista:
        if elemento not in lista_s_duplicados:
            lista_s_duplicados.append(elemento)
    return lista_s_duplicados

lista_normal = [1, 2, 2, 3, 4, 4, 5, 5]
lista_s_duplicados = eliminar_los_duplicados(lista)
print(f"Lista normal: {lista_normal}")
print(f"Lista sin duplicados: {lista_s_duplicados}")