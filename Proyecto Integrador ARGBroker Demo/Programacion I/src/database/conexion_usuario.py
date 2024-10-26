from .conexion_database import DatabaseConnection
from ..interfaces.interface_conexion_database_usuario import InterfaceConexionDatabaseUsuario

class ConexionDatabaseUsuario(InterfaceConexionDatabaseUsuario):
    def __init__(self,connection:DatabaseConnection):
        self.connection=connection.connection_database()
    def add(self,objeto):
        try:
            with self.connection.cursor() as cursor:
                if isinstance(objeto, dict):  #Si el objeto ya es un diccionario se deja asi si no se lo convierte en diccionario
                    objeto_final = objeto
                else:
                    objeto_final = objeto.__dict__
                valores = list(objeto_final.values())
                placeholders = ', '.join(['%s'] * len(valores))
                query=f"""
                INSERT INTO Usuarios (id_usuario,cuil, nombre, apellido, email, contraseña,perfil)
                VALUES ({placeholders})
                """
                cursor.execute(query, valores)
                self.save_changes()
                print(f"Datos insertados correctamente en la tabla Usuarios")
                return cursor.lastrowid
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def get_one(self, atributos):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT * FROM Usuarios WHERE
                """
                conditions=[]
                values=[]
                for key, value in atributos.items():
                    conditions.append(f"{key} = %s")
                    values.append(value)
                query += " AND ".join(conditions)
                cursor.execute(query, values)
                resultado=cursor.fetchone()
                return resultado
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def update(self, columna_a_actualizar, nuevo_valor, condicion_columna, condicion_valor):
        try:
            with self.connection.cursor() as cursor:
                query = f"""
                UPDATE Usuarios
                SET {columna_a_actualizar} = %s
                WHERE {condicion_columna} = %s
                """
                cursor.execute(query, (nuevo_valor, condicion_valor))
                self.save_changes()
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def save_changes(self):
        self.connection.commit()