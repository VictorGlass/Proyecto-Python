'''
Dia 31 - Fusionar Diccionarios.

Fusionar dos diccionarios.
'''

#SOLUCION:

'''
Para fusionar dos diccionarios en Python,
podemos utilizar el operador '|'.
'''

def fusionar_diccionarios(dict1, dict2):
    #Fusionamos los diccionarios usando |:
    diccionario_fusionado = dict1 | dict2
    return diccionario_fusionado

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

resultado = fusionar_diccionarios(dict1, dict2)
print(resultado)

