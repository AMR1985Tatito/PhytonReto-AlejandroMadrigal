'''
Ejercicio 2. Función calcular_promedio
Crea una función que calcule el promedio de una lista de números.
'''

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


numeros = [15, 26, 37, 48, 59]
promedio = calcular_promedio(numeros)
print("El promedio de la lista es:", promedio)