'''
Dia 33 - Operaciones de archivo: Escritura.

Escribir datos en un archivo de texto.
'''

#SOLUCION:

'''
Para escribir datos en un archivo de texto en Python,
podemos usar la funcion open() con el modo de escritura 'w'.

Este modo sobreescribira si el archivo ya existe, o creara
un nuevo archivo si no lo hace.
'''

def escribir_en_archivo(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(datos)
        print(f"Datos escritos correctamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

datos = "Dia 33 - Escribiendo en archivos\nEste es un ejemplo de escritura en un archivo de texto"

escribir_en_archivo("Users\Victor_Dev\OneDrive - INACAP\Desktop\Formacion\Python\100DaysOfCodes - Python\Proyecto Python\33_Operaciones de archivo Escritura\nuevo_archivo", datos)