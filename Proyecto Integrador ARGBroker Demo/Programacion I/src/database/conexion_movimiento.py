from .conexion_database import DatabaseConnection
from ..interfaces.interface_conexion_database_movimiento import InterfaceConexionDatabaseMovimiento

class ConexionDatabaseMovimiento(InterfaceConexionDatabaseMovimiento):
    def __init__(self,connection:DatabaseConnection):
        self.connection=connection.connection_database()
    def calcular_saldo(self,id):
        try:
            self.connection.reconnect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT 
                        COALESCE(m.total_movimiento, 0) + COALESCE(o.total_operacion, 0) AS BalanceTotal
                    FROM 
                        (SELECT id_usuario, SUM(monto) AS total_movimiento
                        FROM Movimiento
                        WHERE id_usuario = %s
                        GROUP BY id_usuario) AS m
                    LEFT JOIN 
                        (SELECT id_usuario,
                                SUM(CASE 
                                        WHEN tipo = 'compra' THEN -cantidad * precio_unit
                                        WHEN tipo = 'venta' THEN cantidad * precio_unit
                                    END) AS total_operacion
                        FROM Operacion
                        WHERE id_usuario = %s
                        GROUP BY id_usuario) AS o
                    ON m.id_usuario = o.id_usuario;

                """
                values = (id,id)
                cursor.execute(query, values)
                resultado = cursor.fetchone()
                return int(resultado[0]) if resultado else 0
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
            return 0
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return 0

    def registrar_ingreso(self,monto,id,mensaje=""):
        if monto > 0:
            try:
                with self.connection.cursor() as cursor:
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
            except self.connection.Error as e:
                print(f"Error en la base de datos: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        else:
            return False
        
    def registrar_egreso(self,monto,id):
        if monto > 0 and monto <= self.calcular_saldo(id):
            try:
                with self.connection.cursor() as cursor:
                    query = """
                        INSERT INTO Movimiento (id_usuario, fecha, monto)
                        VALUES (%s, NOW(), %s)
                    """
                    values=(id,-monto)
                    cursor.execute(query, values)
                    self.save_changes()
                    print(f"Egreso registrado: ${monto}")
            except self.connection.Error as e:
                print(f"Error en la base de datos: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        else:
            return False
    def save_changes(self):
        self.connection.commit()
        