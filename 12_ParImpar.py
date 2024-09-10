'''
Dia 12 - Par-impar.

1. Escribe un programa para comprobar si un numero es par o impar. 
'''

#SOLUCION:

#FORMA 1 usando if-else
print("Forma 1")
numero_usuario = int(input("Ingresa un numero: "))

if numero_usuario % 2 == 0:
    print("El numero es par")
else:
    print("No es par")

#FORMA2 usando while
print()
print("Forma 2")
num = int(input("Ingresa un numero: "))

while True:
    if num % 2 == 0:
        print(f"Ingresaste un {num} y es par")
    else:
        print(f"Ingresaste un {num} y no es par")
    break

#FORMA 3 usando funcion
print()
print("Forma 3")
usuario = int(input("Ingresa otro numero: "))
def es_par(usuario):
    if usuario % 2 == 0:
        return "Es par"
    else:
        return "No es par"

print(es_par(usuario))



