import re
import mysql.connector
from mysql.connector import Error

class Usuario:
    def __init__(self, cuil, nombre, apellido, email, contraseña, perfil):
        self.cuil = cuil
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.perfil = perfil

def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host='camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com',
            database='argbroker',
            user='admin',
            password='8xXnpE4d9BXXeheu2pWH'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def email_existe(connection, email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE email = %s", (email,))
        resultado = cursor.fetchone()
    return resultado[0] > 0

def cuil_existe(connection, cuil):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE cuil = %s", (cuil,))
        resultado = cursor.fetchone()
    return resultado[0] > 0

def solicitar_datos(connection):
    # Validación de CUIL
    while True:
        cuil = input("Ingrese su CUIL (11 dígitos): ")
        if len(cuil) == 11 and cuil.isdigit():
            if not cuil_existe(connection, cuil):
                break
            else:
                print("CUIL ya registrado. Intente con otro.")
        else:
            print("CUIL inválido. Debe contener exactamente 11 dígitos.")

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
        if re.match(r'^[\w\.-]+@(gmail\.com|hotmail\.com|yahoo\.com)$', email):
            if not email_existe(connection, email):
                break
            else:
                print("El email ya está registrado. Intente con otro.")
        else:
            print("Correo electrónico inválido. Solo se permiten dominios @gmail.com, @hotmail.com o @yahoo.com.")

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
        
    while True:
        perfil = input("Ingrese el tipo de perfil de usuario: ")
        if not perfil in ["conservador","medio","agresivo"]:
            print("El tipo de perfil no es permitido, vuelva a ingresar")
        else:
            break

    return Usuario(cuil, nombre, apellido, email, contraseña, perfil)

def insertar_datos(connection, perfil, nombre, apellido, cuil, email):
    cursor = connection.cursor()
    insert_query = """
            INSERT INTO Usuarios ( perfil, nombre, apellido, cuil, email) 
            VALUES (%s, %s, %s, %s, %s)
        """
        # Asumiendo que 'id_usuarios' es un autoincremento, omitirlo al insertar
    values = (perfil, nombre, apellido, cuil, email)
    cursor.execute(insert_query, values)
    connection.commit()
    
    


# Conectar a la base de datos
connection = conectar_bd()

if connection:
    # Crear un nuevo usuario con los datos recolectados
    usuario = solicitar_datos(connection)

    # Mostrar los datos del usuario (sin la contraseña)
    print("\nDatos del usuario:")
    print(f"CUIL: {usuario.cuil}")
    print(f"Nombre: {usuario.nombre}")
    print(f"Apellido: {usuario.apellido}")
    print(f"Email: {usuario.email}")
    insertar_datos(connection, usuario.perfil, usuario.nombre, usuario.apellido, usuario.cuil, usuario.email)
    # Cerrar la conexión a la base de datos
    connection.close()
    