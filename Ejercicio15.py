'''
Ejercicio 15. Clase UsuarioBanco

Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si
tiene o no cuenta corriente. Proporciona métodos para realizar operaciones
como retirar dinero, transferir dinero desde otro usuario y agregar dinero al
saldo.

Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del
usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia
desde otro usuario al usuario actual. Lanzará un error en caso de no poder
hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del
usuario.

Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo
inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Alicia".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
'''
class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo para realizar la operación.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.tiene_cuenta_corriente or not otro_usuario.tiene_cuenta_corriente:
            raise ValueError("Al menos uno de los usuarios no tiene cuenta corriente para realizar la transferencia.")
        if cantidad > self.saldo:
            print("No hay suficiente saldo para realizar la transferencia.")
            return
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad


# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
usuario_alicia = UsuarioBanco("Alicia", 100, True)
usuario_bob = UsuarioBanco("Bob", 50, True)
print("1. Crear dos usuarios:")
print(f"Usuario Alicia - Saldo inicial: {usuario_alicia.saldo}, Cuenta corriente: {usuario_alicia.tiene_cuenta_corriente}")
print(f"Usuario Bob - Saldo inicial: {usuario_bob.saldo}, Cuenta corriente: {usuario_bob.tiene_cuenta_corriente}")

# 2. Agregar 20 unidades de saldo de "Alicia".
print("\n2. Agregar 20 unidades de saldo a Alicia.")
usuario_alicia.agregar_dinero(20)
print("Saldo actual de Alicia:", usuario_alicia.saldo)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
print("\n3. Hacer una transferencia de 80 unidades desde Bob a Alicia.")
usuario_bob.transferir_dinero(usuario_alicia, 80)
print("Saldo actual de Alicia:", usuario_alicia.saldo)
print("Saldo actual de Bob:", usuario_bob.saldo)

# 4. Retirar 50 unidades de saldo a "Alicia".
print("\n4. Retirar 50 unidades de saldo a Alicia.")
usuario_alicia.retirar_dinero(50)
print("Saldo actual de Alicia:", usuario_alicia.saldo)