from ..interfaces.interface_conexion_database_accion import InterfaceConexionDatabaseAccion
from .conexion_database import DatabaseConnection

class ConexionDatabaseAccion(InterfaceConexionDatabaseAccion):
    def __init__(self, connection:DatabaseConnection):
        self.connection=connection.connection_database()  
    def get_accion(self,id):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT * FROM Accion WHERE id_accion = %s
                """
                values=(id,)
                cursor.execute(query, values)
                resultado=cursor.fetchone()
                return resultado
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def get_all_acciones(self):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT * FROM Accion
                """
                cursor.execute(query, ())
                resultado=cursor.fetchall()
                return resultado
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")