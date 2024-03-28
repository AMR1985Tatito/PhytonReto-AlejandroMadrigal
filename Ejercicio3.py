'''
Ejercicio 3. Función encontrar_duplicado
Crea una función que busque y devuelva el primer elemento duplicado en una
lista dada.
'''

def encontrar_duplicado(lista):
    buscar_duplicados = set()
    for elemento in lista:
        if elemento in buscar_duplicados:
            return elemento
        buscar_duplicados.add(elemento)
    return None


numeros = [100, 200, 300, 400, 500, 200, 600]
duplicado = encontrar_duplicado(numeros)
if duplicado is not None:
    print("El primer elemento duplicado es:", duplicado)
else:
    print("No se encontraron elementos duplicados en la lista.")