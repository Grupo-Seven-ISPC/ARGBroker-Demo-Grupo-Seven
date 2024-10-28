from .conexion_database import DatabaseConnection
from ..interfaces.interface_conexion_database_cotizaciones import InterfaceConexionDatabaseCotizaciones

class ConexionDatabaseCotizaciones(InterfaceConexionDatabaseCotizaciones):
    def __init__(self,connection:DatabaseConnection):
        self.connection=connection.connection_database()
    def consultar_simbolo_compra(self,simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT h.precio_compra FROM Cotizaciones h JOIN Accion a ON h.id_accion = a.id_accion 
                    WHERE a.simbolo = %s AND h.dia = CURRENT_DATE()
                """
                values=(simbolo,)
                cursor.execute(query, values)
                resultado=cursor.fetchone()
                if resultado is None:
                    raise ValueError(f"No se encontró ninguna cotización para el símbolo {simbolo}.")
                precio = resultado[0]
                return precio
        except ValueError as ve:
            print(ve)
            return None
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
            return None
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return None

    def consultar_simbolo_venta(self,simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT h.precio_venta FROM Cotizaciones h JOIN Accion a ON h.id_accion = a.id_accion 
                    WHERE a.simbolo = %s AND h.dia = CURRENT_DATE()
                """
                values=(simbolo,)
                cursor.execute(query, values)
                resultado=cursor.fetchone()
                if resultado is None:
                    raise ValueError(f"No se encontró ninguna cotización para el símbolo {simbolo}.")
                precio = resultado[0]
                return precio
        except ValueError as ve:
            print(ve)
            return None
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
            return None
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return None
    