import re
from flask import Flask
from pyngrok import ngrok
import mysql.connector
import threading

class Usuario:
    def __init__(self, cuit, nombre, apellido, email, contraseña):
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host="camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com",
            database="argbroker",
            user="admin",  # Cambia por tu usuario MySQL
            password="8xXnpE4d9BXXeheu2pWH"  # Cambia por tu contraseña MySQL
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def email_existe(connection, email):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    return resultado[0] > 0

def cuit_existe(connection, cuit):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE cuit = %s", (cuit,))
    resultado = cursor.fetchone()
    return resultado[0] > 0

def solicitar_datos(connection):
    # Validación de CUIT
    while True:
        cuit = input("Ingrese su CUIT (11 dígitos): ")
        if len(cuit) == 11 and cuit.isdigit():
            if not cuit_existe(connection, cuit):
                break
            else:
                print("CUIT ya registrado. Intente con otro.")
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

    return Usuario(cuit, nombre, apellido, email, contraseña)

# Conectar a la base de datos
connection = conectar_bd()

"""if connection:
    # Crear un nuevo usuario con los datos recolectados
    usuario = solicitar_datos(connection)

    # Mostrar los datos del usuario
    print("\nDatos del usuario:")
    print(f"CUIT: {usuario.cuit}")
    print(f"Nombre: {usuario.nombre}")
    print(f"Apellido: {usuario.apellido}")
    print(f"Email: {usuario.email}")

    # Cerrar la conexión a la base de datos
    connection.close()
"""