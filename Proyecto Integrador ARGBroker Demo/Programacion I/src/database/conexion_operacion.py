from ..interfaces.interface_conexion_database_operacion import InterfaceConexionDatabaseOperacion
from .conexion_database import connection

class ConexionDatabaseOperacion(InterfaceConexionDatabaseOperacion):
    def __init__(self):
        self.connection=connection
    def save_changes(self):
        self.connection.commit()
    def get_operacion(self, id):
        try:
            cursor = connection.cursor()
            query = """
                SELECT * FROM Operacion WHERE id_operacion = %s
            """
            values=(id,)
            cursor.execute(query, values)
            resultado = cursor.fetchone()
            if resultado:
                return resultado
            else:
                print("Esta operacion no existe")
        except connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def get_operaciones(self, id):
        try:
            cursor = connection.cursor()
            query = """
                SELECT * FROM Operacion WHERE id_usuario = %s
            """
            values=(id,)
            cursor.execute(query, values)
            resultado = cursor.fetchone()
            if resultado:
                return resultado
            else:
                print("Este usuario no posee operaciones realizadas")
        except connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def add_operacion(self, id_estado, id_usuario, id_accion, cantidad , tipo , precio_unit):
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Operacion (fecha, id_estado, id_usuario ,id_accion, cantidad, tipo , precio_unit) 
                VALUES (NOW(),%s, %s, %s ,%s,%s,%s)
            """
            values=(id_estado,id_usuario,id_accion,cantidad,tipo,precio_unit)
            cursor.execute(query, values)
            self.save_changes()
            print(f"Operacion Completada")

        except connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")