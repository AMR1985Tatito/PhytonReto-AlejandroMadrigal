'''
Ejercicio 6. Función buscar_nombre
Crea una función que solicite al usuario ingresar una lista de nombres y luego
solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se
imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza
una excepción.

Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función
funciona correctamente: "Jaime", "Silvia" y "Ana".
'''

def buscar_nombre():
    lista_nombres = input("Ingrese una lista de nombres separados por comas: ").split(",")
    lista_nombres = [nombre.strip() for nombre in lista_nombres]
    
    nombre_buscar = input("Ingrese el nombre que desea buscar: ").strip()
    
    if nombre_buscar in lista_nombres:
        print(f'El nombre "{nombre_buscar}" fue encontrado en la lista.')
    else:
        raise ValueError(f'El nombre "{nombre_buscar}" no fue encontrado en la lista.')

try:
    buscar_nombre()
except ValueError as e:
    print("Error:", e)