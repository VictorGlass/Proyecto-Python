'''
Dia 3 - Entrada y Salida.

1. Escribe un programa que lea la entrada del usuario e imprimalo por consola..
2. Modifique el programa para leer e imprimir entradas de diferentes tipos de datos,
   (numeros enteros, numeros de coma flotante, cadenas).
'''

#SOLUCION:

#1.
nombre_usuario = input("Ingrese su nombre completo: ")
print(f"El nombre ingresado es: {nombre_usuario}, Bienvenido!")

#2.
nombre = input("Ingrese un nuevo nombre: ")
edad = int(input("Ingrese su edad: "))
domicilio = input("Ingrese su domicilio: ")
lugar_trabajo = input("Donde trabajas: ")
sueldo = float(input("Cual es tu sueldo: "))

print()
print(f"Bienvenido {nombre}, tienes {edad} años, vives en {domicilio}, trabajas en {lugar_trabajo} y tu sueldo es: ${sueldo}")


#Datos de Python:

'''
Python ofrece varios metodos para leer diferentes tipos de entradas,
dependiendo del contexto en el que se este trabajando.

Entrada desde el teclado (input):
Es el metodo mas basico y se usa para leer una linea de entrada del usuario.
Devuelve un string que puede ser convertido a otros tipos de datos si es necesario.
**name = input("Cual es su nombre: ")

Lectura de archivos:
open(), se usa para abrir y leer archivos de texto u otros formatos. Hay diferentes modos
como r(lectura), w(escritura). a(adjuntar) y b(modo binario).
**with open('file.txt', 'r') as file:
    content = file.read() /Lee todo el contenido del archivo.
'''