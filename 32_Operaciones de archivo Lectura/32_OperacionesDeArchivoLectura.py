'''
Dia 32 - Operaciones de archivo: Lectura

Leer y mostrar el contenido de un archivo de texto.
'''

#SOLUCION:

'''
Python posee una funcion incorporada llamda open() que se
utiliza para abrir archivos y realizar operaciones sobre ellos.
'''

def leer_archivo(nombre_archivo):
    try:
        #Se abre el archivo en modo de lectura
        with open(nombre_archivo, "r") as archivo:
            #Leemos el contenido completo del archivo:
            contenido = archivo.read()
            #Mostramos el contenido
            print(contenido)
    except FileNotFoundError:
        print(f"Error: el archivo {nombre_archivo} no existe")

#Especificamos la ruta del archivo
leer_archivo("/Users/Victor_Dev/OneDrive - INACAP/Desktop/Formacion/Python/100DaysOfCodes - Python/Proyecto Python/32_Operaciones de archivo Lectura/leeme.txt")


