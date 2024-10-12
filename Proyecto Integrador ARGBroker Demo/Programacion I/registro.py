import re

class Usuario:
    def __init__(self, cuit, nombre, apellido, email, contraseña):
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

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

# Crear un nuevo usuario con los datos recolectados
usuario = solicitar_datos()

# Mostrar los datos del usuario
print("\nDatos del usuario:")
print(f"CUIT: {usuario.cuit}")
print(f"Nombre: {usuario.nombre}")
print(f"Apellido: {usuario.apellido}")
print(f"Email: {usuario.email}")