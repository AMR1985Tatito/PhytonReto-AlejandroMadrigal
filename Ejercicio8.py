'''
Ejercicio 8. Función encontrar_puesto_empleado
Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre completo en la lista y devuelve el puesto del empleado si
está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí.

Caso de uso:
empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
{'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
{'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]
'''

def encontrar_puesto_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        nombre = empleado.get('nombre', '')
        apellido = empleado.get('apellido', '')
        puesto = empleado.get('puesto', '')
        nombre_apellido = nombre + " " + apellido
        if nombre_apellido.lower() == nombre_completo.lower():
            return puesto
    return "La persona no trabaja aquí."


empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
             {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
             {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

nombre_completo_buscar = "Juan García"
puesto_empleado = encontrar_puesto_empleado(nombre_completo_buscar, empleados)
print(f"{nombre_completo_buscar} - {puesto_empleado}")