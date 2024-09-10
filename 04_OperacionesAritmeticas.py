'''
Dia 4 - Operaciones aritmeticas.

1. Escribir un programa que declare dos variables enteras y realizar operaciones
   aritmeticas basicas(suma, resta, multiplicacion, division) sobre ellas. Imprime los resultados en consola.
2. Escribe un programa que calcule el area de un rectangulo.
   Pida al usuario que introduzca la longitud(entero) y el ancho(entero) del rectangulo.
   Calcule el area(largo * ancho) e imprima el resultado.
3. Modifique el programa anterior para leer numeros decimales como el largo y el ancho,
   y genere el area a dos puntos decimales.
'''


#SOLUCION:

#1.
numero1 = 10
numero2 = 10

suma = 10 + 10
resta = 10 - 10
multiplicacion = 10 * 10
division = 10 / 10
print()
print("Bienvenido a ejercicios aritmeticos.")
print(f"Los valores son: {numero1} y {numero2}")
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicacion de {numero1} y {numero2} es: {multiplicacion}")
print(f"La division de {numero1} y {numero2} es: {division}")


#2.
print()
print("Bienvenido! Calculemos un rectangulo!")
longitud = int(input("Introduce la longitud del rectangulo: "))
ancho = int(input("Introduce el ancho del rectangulo: "))
area = longitud * ancho
print(f"El area del rectangulo es: {area}")

#3.
print()
print("Bienvenido! Calculemos un rectangulo con numeros decimales!")
largo = float(input("Introduce la largo del rectangulo: "))
ancho2 = float(input("Introduce el ancho del rectangulo: "))
area2 = largo * ancho2
print(f"El area del rectangulo es: {area2}")


#Datos de Python:

'''
1. Obtenga informacion sobre las opciones de formato, como la precision, la alineacion
  y los decimales, para presentar la salida de forma clara y concisa.

R: En Python es posible controlar el formato de salida de los datos 
   para que sea clara y concisa la informacion, utilizando varias tecnicas.

   El metodo 'format()' permite dar formato a los datos de manera flexible.

   Precision en Decimales:
   valor = 3.14159265358979
   print("Valor con 2 decimales: {:.2f}".format(valor)) /Salida: 3.14


'''