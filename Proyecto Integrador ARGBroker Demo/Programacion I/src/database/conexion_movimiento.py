from .conexion_database import connection
from ..interfaces.interface_conexion_database_movimiento import InterfaceConexionDatabaseMovimiento

class ConexionDatabaseMovimiento(InterfaceConexionDatabaseMovimiento):
    def __init__(self):
        self.connection=connection
    def calcular_saldo(self,id):
        try:
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
        except connection.Error as e:
            print(f"Error en la base de datos: {e}")
            return 0
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return 0

    def registrar_ingreso(self,monto,id,mensaje=""):
        if monto > 0:
            try:
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
            except connection.Error as e:
                print(f"Error en la base de datos: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        else:
            return False
        
    def registrar_egreso(self,monto,id):
        if monto > 0 and monto <= self.calcular_saldo(id):
            try:
                cursor = connection.cursor()
                query = """
                    INSERT INTO Movimiento (id_usuario, fecha, monto)
                    VALUES (%s, NOW(), %s)
                """
                values=(id,-monto)
                cursor.execute(query, values)
                self.save_changes()
                print(f"Egreso registrado: ${monto}")
            except connection.Error as e:
                print(f"Error en la base de datos: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        else:
            return False
    def save_changes(self):
        self.connection.commit()
        
        #Esta funcion tiene que ir en Accion , o en HistorialAcciones
    def consultar_simbolo(self,simbolo):
        try:
            cursor = connection.cursor()
            query = """
                SELECT h.precio FROM HistorialAcciones h JOIN Accion a ON h.id_accion = a.id_accion 
                WHERE a.simbolo = %s AND h.dia = CURRENT_DATE()
            """
            values=(simbolo,)
            cursor.execute(query, values)
            resultado=cursor.fetchone()
            precio = resultado[0]
            print(f"\nEl precio de compra es: {precio}")
            return precio
        except connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")