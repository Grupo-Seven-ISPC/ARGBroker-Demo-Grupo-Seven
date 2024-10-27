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
    def get_cantidad_acciones_disponibles(self,simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT cantidad FROM Accion WHERE simbolo = %s
                """
                cursor.execute(query, (simbolo,))
                resultado=cursor.fetchone()
                return resultado
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def disminuir_cantidad_acciones(self,cantidad_a_restar,simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    UPDATE Accion
                    SET cantidad = cantidad - %s
                    WHERE simbolo = %s
                """
                cursor.execute(query, (cantidad_a_restar,simbolo))
                self.connection.commit()
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def aumentar_cantidad_acciones(self,cantidad_a_aumentar,simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    UPDATE Accion
                    SET cantidad = cantidad + %s
                    WHERE simbolo = %s
                """
                cursor.execute(query, (cantidad_a_aumentar,simbolo))
                self.connection.commit()
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def get_cantidad_acciones_adquiridas_usuario(self,id_usuario):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT 
                        a.simbolo AS Accion,
                        SUM(CASE 
                                WHEN o.tipo = 'compra' THEN o.cantidad 
                                WHEN o.tipo = 'venta' THEN -o.cantidad
                            END) AS Cantidad
                    FROM 
                        Operacion o
                    JOIN 
                        Accion a ON o.id_accion = a.id_accion
                    WHERE 
                        o.id_usuario = %s
                    GROUP BY 
                        a.simbolo
                    HAVING 
                        Cantidad > 0;
                """
                cursor.execute(query, (id_usuario,))
                resultado=cursor.fetchall()
                return resultado
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def get_cantidad_acciones_adquiridas_usuario_por_simbolo(self, id_usuario, simbolo):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT 
                        a.id_accion AS IdAccion,
                        a.simbolo AS Accion,
                        SUM(CASE 
                                WHEN o.tipo = 'compra' THEN o.cantidad 
                                WHEN o.tipo = 'venta' THEN -o.cantidad
                            END) AS Cantidad
                    FROM 
                        Operacion o
                    JOIN 
                        Accion a ON o.id_accion = a.id_accion
                    WHERE 
                        o.id_usuario = %s
                        AND a.simbolo = %s
                    GROUP BY 
                        a.id_accion, a.simbolo
                    HAVING 
                        Cantidad > 0;

                """
                cursor.execute(query, (id_usuario, simbolo))
                resultado = cursor.fetchone() 
                return resultado if resultado else (simbolo, 0) 
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
