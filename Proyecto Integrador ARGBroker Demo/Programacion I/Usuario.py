from HelperUsuario import UsuarioHelper
from Connection import ConexionDatabase
from datetime import datetime

class Usuario:
    def __init__(self, id_usuario,cuil, nombre, apellido, email, contraseña,perfil):
        self.id_usuario=id_usuario
        self.cuil = cuil
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.perfil=perfil
        self.conexion=ConexionDatabase()
    @classmethod
    def convertir_tupla_diccionario(objeto, datos):
        id_usuario, cuil, nombre, apellido, email, perfil, contraseña = datos
        return objeto(id_usuario, cuil, nombre, apellido, email, contraseña, perfil)
    
    def registrar_ingreso(self, monto):
        if monto > 0:
            movimiento_ingreso={
                "id_usuario":self.id_usuario,
                "fecha":datetime.now(),
                "monto":monto
            }
            self.conexion.add_to_database("Movimiento",movimiento_ingreso)
            print(f"Ingreso registrado: ${monto}")       
        else:
            print("El monto debe ser mayor a 0 para registrar un ingreso.")
            return

    def registrar_egreso(self, monto,conexion):
        if monto > 0 and monto <= self.calcular_saldo(conexion):
            movimiento_egreso={
                "id_usuario":self.id_usuario,
                "fecha":datetime.now(),
                "monto":monto
            }
            self.conexion.add_to_database("Movimiento",movimiento_egreso)
            print(f"Egreso registrado: ${monto}")
        else:
            print("Egreso no válido. Verifique el monto.")
            return

    def calcular_saldo(self,connection):
        cursor = connection.cursor()
        calcular_saldo_query = """
            SELECT COALESCE(SUM(m.monto),0) + COALESCE(SUM(CASE WHEN o.tipo = 'compra' THEN -o.cantidad * o.precio_unit WHEN o.tipo = 'venta' THEN o.cantidad * o.precio_unit END) ,0) AS BalanceTotal
            FROM Movimiento m 
            LEFT JOIN Operacion o 
            ON m.id_usuario = o.id_usuario 
            WHERE m.id_usuario = %s
            GROUP BY m.id_usuario
        """
        values = (self.id_usuario,)
        cursor.execute(calcular_saldo_query, values)
        resultado = cursor.fetchone()
        if resultado :
            return int(resultado[0]) 
        else:
            print("No tienes saldo disponible")
            return 0
