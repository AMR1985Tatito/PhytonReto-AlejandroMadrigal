'''
Ejercicio 4. Función enmascarado_datos
Crea una función que convierta una variable en una cadena de texto y
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
'''

def enmascarado_datos(variable):
    variable_str = str(variable)
    longitud = len(variable_str)
    enmascarado = '#' * (longitud - 4) + variable_str[-4:]
    return enmascarado


numero_tarjeta = 1234567890123456
enmascarado = enmascarado_datos(numero_tarjeta)
print("Número de tarjeta enmascarado:", enmascarado)