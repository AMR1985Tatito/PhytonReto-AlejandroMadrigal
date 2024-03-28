'''
Ejercicio 10. Función resto_division usando lambdas
Crea una función que calcule el resto de la división entre dos números dados.
'''

resto_division = lambda x, y: x % y


dividendo = 10
divisor = 3
resultado = resto_division(dividendo, divisor)
print(f"El resto de la división entre {dividendo} y {divisor} es", resultado)