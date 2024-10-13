import re

# Simulación de una base de datos de usuarios
usuarios_registrados = [
    {"email": "juan@example.com", "contraseña": "Password123", "nombre": "Juan"},
    {"email": "maria@example.com", "contraseña": "Maria2023", "nombre": "Maria"},
]

# Función para iniciar sesión
def iniciar_sesion():
    print("\nFormulario de Inicio de Sesión:")
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    # Buscar al usuario por su correo y contraseña
    for usuario in usuarios_registrados:
        if usuario["email"] == email and usuario["contraseña"] == contraseña:
            print(f"\nInicio de sesión exitoso. Bienvenido, {usuario['nombre']}!")
            return True
    print("\nCorreo o contraseña incorrectos. Intente nuevamente.")
    return False

# Función para recuperar contraseña
def recuperar_contraseña():
    print("\nRecuperar contraseña:")
    email = input("Ingrese su correo electrónico registrado: ")

    # Buscar el correo en la lista de usuarios registrados
    for usuario in usuarios_registrados:
        if usuario["email"] == email:
            print(f"Se ha enviado un enlace de recuperación a su correo: {email}.")
            # Simulación de envío de correo (se podría integrar una función real para enviar correos)
            print(f"Contraseña actual: {usuario['contraseña']}")  # Para la simulación mostramos la contraseña
            return

    print("El correo ingresado no está registrado en el sistema.")

# Flujo principal para permitir inicio de sesión o recuperación de contraseña
if __name__ == "__main__":
    while True:
        print("\n1. Iniciar sesión")
        print("2. Recuperar contraseña")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            recuperar_contraseña()
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


