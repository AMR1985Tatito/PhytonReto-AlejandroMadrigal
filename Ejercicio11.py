'''
Ejercicio 11. Función numeros_pares usando lambdas y
filter
Crea una función lambda que filtre los números pares de una lista dada.

Caso de uso: lista_numeros = [24, 56, 2.3, 19, -1, 0]
'''

lista_numeros = [24, 56, 2.3, 19, -1, 0]
filtrar_pares = lambda x: x % 2 == 0 and isinstance(x, int)
numeros_pares = list(filter(filtrar_pares, lista_numeros))


print("Números pares en la lista ", numeros_pares)