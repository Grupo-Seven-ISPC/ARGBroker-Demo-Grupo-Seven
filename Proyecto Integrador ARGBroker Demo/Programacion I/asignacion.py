import re

class Usuario:
    def __init__(self, cuit, nombre, apellido, email, contraseña):
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.transacciones = []  # Lista para almacenar ingresos y egresos

    def registrar_ingreso(self, monto):
        """Registra un ingreso de dinero."""
        if monto > 0:
            self.transacciones.append(monto)
            print(f"Ingreso registrado: ${monto}")
        else:
            print("El monto debe ser mayor a 0 para registrar un ingreso.")

    def registrar_egreso(self, monto):
        """Registra un egreso de dinero."""
        if monto > 0 and monto <= self.calcular_saldo():
            self.transacciones.append(-monto)  # Los egresos se registran como números negativos
            print(f"Egreso registrado: ${monto}")
        else:
            print("Egreso no válido. Verifique el monto.")

    def calcular_saldo(self):
        """Calcula el saldo actual sumando los ingresos y restando los egresos."""
        return sum(self.transacciones)

def solicitar_datos():
    # Validación de CUIT
    while True:
        cuit = input("Ingrese su CUIT (11 dígitos): ")
        if len(cuit) == 11 and cuit.isdigit():
            break
        else:
            print("CUIT inválido. Debe contener exactamente 11 dígitos.")

    # Solicitar nombre y convertir a minúsculas
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre.isalpha():
            nombre = nombre.lower()  # Convertir a minúsculas
            break
        else:
            print("El nombre debe contener solo letras.")

    # Solicitar apellido y convertir a minúsculas
    while True:
        apellido = input("Ingrese su apellido: ").strip()
        if apellido.isalpha():
            apellido = apellido.lower()  # Convertir a minúsculas
            break
        else:
            print("El apellido debe contener solo letras.")

    # Validación de email
    while True:
        email = input("Ingrese su email: ")
        # Verifica que el email tenga un formato válido
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            break
        else:
            print("Correo electrónico inválido. Asegúrate de usar un formato correcto (ejemplo: correo@dominio.com).")

    # Validación de contraseña
    while True:
        contraseña = input("Ingrese su contraseña (mínimo 8 caracteres, al menos una mayúscula y una minúscula): ")
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        elif not re.search("[A-Z]", contraseña):
            print("La contraseña debe contener al menos una letra mayúscula.")
        elif not re.search("[a-z]", contraseña):
            print("La contraseña debe contener al menos una letra minúscula.")
        else:
            break

    return Usuario(cuit, nombre, apellido, email, contraseña)

# Lista de usuarios registrados
usuarios_registrados = []

# Función para registrar nuevos usuarios
def registrar_usuario():
    usuario = solicitar_datos()
    usuarios_registrados.append(usuario)
    print(f"\nEl usuario {usuario.nombre} ha sido registrado con éxito.")
    return usuario

# Función para iniciar sesión
def iniciar_sesion():
    print("\nFormulario de Inicio de Sesión:")
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    # Buscar al usuario por su correo y contraseña
    for usuario in usuarios_registrados:
        if usuario.email == email and usuario.contraseña == contraseña:
            print(f"\nInicio de sesión exitoso. Bienvenido, {usuario.nombre}!")
            return usuario
    print("\nCorreo o contraseña incorrectos. Intente nuevamente.")
    return None

# Flujo del programa
if __name__ == "__main__":
    print("Bienvenido al sistema.")
    
    while True:
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario_activo = iniciar_sesion()
            if usuario_activo:
                while True:
                    print("\n1. Ver saldo actual")
                    print("2. Registrar ingreso")
                    print("3. Registrar egreso")
                    print("4. Cerrar sesión")
                    opcion_usuario = input("Seleccione una opción: ")

                    if opcion_usuario == "1":
                        print(f"Saldo actual: ${usuario_activo.calcular_saldo()}")
                    elif opcion_usuario == "2":
                        monto = float(input("Ingrese el monto del ingreso: "))
                        usuario_activo.registrar_ingreso(monto)
                    elif opcion_usuario == "3":
                        monto = float(input("Ingrese el monto del egreso: "))
                        usuario_activo.registrar_egreso(monto)
                    elif opcion_usuario == "4":
                        print("Cerrando sesión...")
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")
        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

