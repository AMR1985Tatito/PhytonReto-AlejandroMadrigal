'''
Ejercicio 16. Función procesar_texto
Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras
funciones que tenemos que definir primero y llamar dentro de la función
procesar_texto .

Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que
aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original
del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo
de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.
Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre
"contar", "reemplazar", "eliminar") y un número de argumentos variable
según la opción indicada.

Caso de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
Dado el texto de ejemplo, llama a la función procesar_texto para probar sus
funcionalidades:
Cuenta el número de veces que aparece cada palabra.
Reemplaza la palabra texto por relato.
Elimina la palabra ejemplo.
'''

def contar_palabras(texto):
    palabras = texto.split()
    conteo_palabras = {}
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
    return conteo_palabras

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se esperan dos argumentos para la opción 'reemplazar'.")
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se espera un argumento para la opción 'eliminar'.")
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida. Las opciones válidas son 'contar', 'reemplazar' y 'eliminar'.")


# Caso de uso
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

# Cuenta el número de veces que aparece cada palabra.
print("Conteo de palabras:")
print(procesar_texto(texto, "contar"))

# Reemplaza la palabra 'texto' por 'relato'.
texto_reemplazado = procesar_texto(texto, "reemplazar", "texto", "relato")
print("\nTexto con palabras reemplazadas:")
print(texto_reemplazado)

# Elimina la palabra 'ejemplo'.
texto_sin_ejemplo = procesar_texto(texto, "eliminar", "ejemplo")
print("\nTexto con la palabra 'ejemplo' eliminada:")
print(texto_sin_ejemplo)