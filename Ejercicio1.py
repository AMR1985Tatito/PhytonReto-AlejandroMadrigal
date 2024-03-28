'''
Ejercicio 1. Función contar_caracteres
Crea una función que cuente el número de caracteres en una cadena de texto
dada.
'''

def contar_caracteres(cadena):
    return len(cadena)

texto = "Me encanta el Master"
resultado = contar_caracteres(texto)
print("Número de caracteres:", resultado)