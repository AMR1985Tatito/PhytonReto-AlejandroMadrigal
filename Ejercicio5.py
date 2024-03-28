'''
Ejercicio 5. Función es_anagrama
Crea una función que determine si dos palabras son anagramas, es decir, si
están formadas por las mismas letras pero en diferente orden.
'''

def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    if len(palabra1) != len(palabra2):
        return False
    
    return sorted(palabra1) == sorted(palabra2)


palabra_1 = "llenaba"
palabra_2 = "ballena"
if es_anagrama(palabra_1, palabra_2):
    print(f'"{palabra_1}" y "{palabra_2}" son anagramas.')
else:
    print(f'"{palabra_1}" y "{palabra_2}" no son anagramas.')