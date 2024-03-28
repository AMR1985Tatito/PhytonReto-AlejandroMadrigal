'''
Ejercicio 14. No te vayas por las ramas
Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los
métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e
info_arbol . El objetivo es implementar estos métodos para manipular la
estructura del árbol.

Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco
en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de
longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la
longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición
específica.
6. Implementar el método info_arbol para devolver información sobre la
longitud del tronco, el número de ramas y las longitudes de las mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
'''

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("La posición de la rama es inválida.")

    def info_arbol(self):
        info = f"El árbol tiene una longitud de {self.tronco}, "
        info += f"tiene {len(self.ramas)} ramas, con las siguientes longitudes: "
        for i in range(len(self.ramas)):
            info += f"rama_{i+1}: {self.ramas[i]}, "
        return info[:-2]


arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(1)
print(arbol.info_arbol())
