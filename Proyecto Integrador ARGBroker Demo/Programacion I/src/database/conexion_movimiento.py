from .conexion_database import connection
from ..interfaces.interface_conexion_database_movimiento import InterfaceConexionDatabaseMovimiento

class ConexionDatabaseMovimiento(InterfaceConexionDatabaseMovimiento):
    def __init__(self):
        self.connection=connection
    def calcular_saldo(self,id):
        cursor = connection.cursor()
        query = """
            SELECT COALESCE(SUM(m.monto),0) + COALESCE(SUM(CASE WHEN o.tipo = 'compra' THEN -o.cantidad * o.precio_unit WHEN o.tipo = 'venta' THEN o.cantidad * o.precio_unit END) ,0) AS BalanceTotal
            FROM Movimiento m 
            LEFT JOIN Operacion o 
            ON m.id_usuario = o.id_usuario 
            WHERE m.id_usuario = %s
            GROUP BY m.id_usuario
        """
        values = (id,)
        cursor.execute(query, values)
        resultado = cursor.fetchone()
        if resultado :
            return int(resultado[0]) 
        else:
            print("No tienes saldo disponible")
            return 0

    def registrar_ingreso(self,monto,id,mensaje=""):
        if monto > 0:
            cursor = connection.cursor()
            query = """
                INSERT INTO Movimiento (id_usuario, fecha, monto)
                VALUES (%s, NOW(), %s)
            """
            values=(id,monto)
            cursor.execute(query, values)
            self.save_changes()
            if len(mensaje)==0:
                print(f"Ingreso registrado: ${monto}")
            else:
                print("Capital Inicial Asginado")
        else:
            return False
        
    def registrar_egreso(self,monto,id):
        if monto > 0 and monto <= self.calcular_saldo(id):
            cursor = connection.cursor()
            query = """
                INSERT INTO Movimiento (id_usuario, fecha, monto)
                VALUES (%s, NOW(), %s)
            """
            values=(id,-monto)
            cursor.execute(query, values)
            self.save_changes()
            print(f"Egreso registrado: ${monto}")    
        else:
            return False
    def save_changes(self):
        self.connection.commit()