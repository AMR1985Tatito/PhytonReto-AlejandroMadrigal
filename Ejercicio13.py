'''
Ejercicio 13. Función sumar_listas usando lambdas
Crea una función lambda que sume elementos correspondientes de dos listas dadas.

Caso de uso:
lista_numeros_1 = [1, 4, 5, 6 , 7 , 7] ;
lista_numeros_2 = [3, 11, 34, 56]
'''

lista_numeros_1 = [1, 4, 5, 6, 7, 7]
lista_numeros_2 = [3, 11, 34, 56]
sumar_listas = lambda x, y: x + y
resultado = list(map(sumar_listas, lista_numeros_1, lista_numeros_2))


print("La suma de elementos correspondientes es ", resultado)