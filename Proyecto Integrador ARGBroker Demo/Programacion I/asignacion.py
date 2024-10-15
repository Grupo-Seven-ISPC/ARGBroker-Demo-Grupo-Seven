import re
from helpers.helpers import *
from helpers.prueba import *
# from helpers.envio import *
import mysql.connector


connection = mysql.connector.connect(
            host='camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com',
            database='argbroker',
            user='admin',
            password='8xXnpE4d9BXXeheu2pWH'
        )
class Usuario:
    def __init__(self, id, cuit, nombre, apellido, email, contraseña, perfil):
        self.id = id
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.perfil = perfil

    def registrar_ingreso(self, monto):
        """Registra un ingreso de dinero."""
        if monto > 0:
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO Movimiento (id_usuario, fecha, monto)
                VALUES (%s, NOW(), %s)
            """
            # Asumiendo que 'id_usuarios' es un autoincremento, omitirlo al insertar
            values = (self.id, monto)
            cursor.execute(insert_query, values)
            connection.commit()
            print(f"Ingreso registrado: ${monto}")       
        else:
            print("El monto debe ser mayor a 0 para registrar un ingreso.")

    def registrar_egreso(self, monto):
        """Registra un egreso de dinero."""
        if monto > 0 and monto <= self.calcular_saldo():
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO Movimiento (id_usuario, fecha, monto)
                VALUES (%s, NOW(), %s)
            """
            # Asumiendo que 'id_usuarios' es un autoincremento, omitirlo al insertar
            values = (self.id, -monto)
            cursor.execute(insert_query, values)
            connection.commit()
            print(f"Egreso registrado: ${monto}")
        else:
            print("Egreso no válido. Verifique el monto.")

    def calcular_saldo(self):
        """Calcula el saldo actual sumando los ingresos y restando los egresos."""
        cursor = connection.cursor()

        calcular_saldo_query = """
            SELECT COALESCE(SUM(m.monto),0) + COALESCE(SUM(CASE WHEN o.tipo = 'compra' THEN -o.cantidad * o.precio_unit WHEN o.tipo = 'venta' THEN o.cantidad * o.precio_unit END) ,0) AS BalanceTotal
            FROM Movimiento m 
            LEFT JOIN Operacion o 
            ON m.id_usuario = o.id_usuario 
            WHERE m.id_usuario = %s
            GROUP BY m.id_usuario
        """
        values = (self.id,)
        cursor.execute(calcular_saldo_query, values)
        resultado = cursor.fetchone()

        return int(resultado[0])

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

    while True:
        perfil = input("Ingrese el tipo de perfil de usuario: ")
        if not perfil in ["conservador","medio","agresivo"]:
            print("El tipo de perfil no es permitido, vuelva a ingresar")
        else:
            break

    return Usuario(0, cuit, nombre, apellido, email, contraseña, perfil)

# Lista de usuarios registrados
# usuarios_registrados = []

# Función para registrar nuevos usuarios
def registrar_usuario():
    usuario = solicitar_datos()

    cursor = connection.cursor()
    insert_query = """
        INSERT INTO Usuarios (perfil, nombre, apellido, cuil, email, contraseña) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    # Asumiendo que 'id_usuarios' es un autoincremento, omitirlo al insertar
    values = (usuario.perfil, usuario.nombre, usuario.apellido, usuario.cuit, usuario.email, usuario.contraseña)
    cursor.execute(insert_query, values)
    connection.commit()

    print(f"\nEl usuario {usuario.nombre} ha sido registrado con éxito.")
    return usuario

# Función para iniciar sesión
intentos_contraseña= IntentosContraseña()


def iniciar_sesion():
    print("\nFormulario de Inicio de Sesión:")

    resultado = None
    
    while resultado is None:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        cursor = connection.cursor()
        insert_query = """
            SELECT * FROM Usuarios WHERE email = %s AND contraseña = %s 
        """
        values = (email, contraseña)
        cursor.execute(insert_query, values)
        resultado=cursor.fetchone()

        connection.commit()
    return Usuario(resultado[0], resultado[4], resultado[2], resultado[3], resultado[5], resultado[6], resultado[1])
    

def recuperar_contraseña(email):
    print("\n¿Has olvidado tu contraseña?")
    print("\n1. Reestablecer Contraseña")
    print("\n2. Volver a iniciar sesion")
    contraseña_olvidada= input("\nSeleccione una opcion: ")
    if contraseña_olvidada == "1":
        usuario_a_buscar=buscar_usuario_por_mail(usuarios_registrados,email)
        if usuario_a_buscar:
            print("Usuario encontrado exitosamente")
            print("Se ha enviado a tu correo electronico el token para el cambio de contraseña")
            token_usuario=generar_token()
            enviar_mail_recuperacion(email,token_usuario)
            token_confirmacion=input("Ingrese el token de seguridad: ")
            if token_usuario == token_confirmacion:
                contraseña_nueva=input("Ingrese la nueva contraseña :")
                contraseña_nueva_repetida=input("Ingrese la nueva contraseña de nuevo :")
                if contraseña_nueva == contraseña_nueva_repetida:
                    #Aca va la logica para cuando tengamos la conexion con la BD
                    print("Contraseña cambiada correctamente")
                else:
                    print("Las contraseñas no coinciden")
                    
            else:
                print("Codigo de verificacion incorrecto")

        else:
            print("No se encontro al usuario con ese email")
    elif contraseña_olvidada == "2":
     return iniciar_sesion()
    else:
        print("Opción no válida. Intente nuevamente.")


# Flujo del programa
if __name__ == "__main__":
    print("Bienvenido al sistema.")
    
    while True:
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Olvido su contraseña?")
        print("4. Salir")
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
            email= input("Ingrese el email con el cual esta asociado su cuenta : ")
            recuperar_contraseña(email)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# 