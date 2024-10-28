from ..interfaces.interface_conexion_database_operacion import InterfaceConexionDatabaseOperacion
from .conexion_database import DatabaseConnection

class ConexionDatabaseOperacion(InterfaceConexionDatabaseOperacion):
    def __init__(self,connection:DatabaseConnection):
        self.connection=connection.connection_database()
    def save_changes(self):
        try:
            self.connection.commit()
        except Exception as e:
            print(f"Error al confirmar los cambios: {e}")
    def get_operacion(self, id):
        try:
            with self.connection.cursor() as cursor:
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
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def get_operaciones(self, id):
        try:
            with self.connection.cursor() as cursor:
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
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def add_operacion(self, id_estado, id_usuario, id_accion, cantidad , tipo , precio_unit):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    INSERT INTO Operacion (fecha, id_estado, id_usuario ,id_accion, cantidad, tipo , precio_unit) 
                    VALUES (NOW(),%s, %s, %s ,%s,%s,%s)
                """
                values=(id_estado,id_usuario,id_accion,cantidad,tipo,precio_unit)
                cursor.execute(query, values)
                self.save_changes()
                print(f"Operacion Completada")
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    def obtener_historial_transacciones(self, id_usuario):
        try:
            with self.connection.cursor() as cursor:
                consulta = """
                SELECT 
                    O.id_operacion,
                    O.fecha,
                    O.cantidad,
                    O.tipo,
                    O.precio_unit,
                    A.nombre AS nombre_accion,
                    A.simbolo AS simbolo_accion,
                    E.estado AS estado_operacion
                FROM 
                    Operacion O
                JOIN 
                    Accion A ON O.id_accion = A.id_accion
                JOIN 
                    Estado E ON O.id_estado = E.id_estado
                WHERE 
                    O.id_usuario = %s;
                """
                cursor.execute(consulta, (id_usuario,))
                resultados = cursor.fetchall()

                if resultados:
                    for transaccion in resultados:
                        print(f"ID Operación: {transaccion[0]}, Fecha: {transaccion[1]}, "
                              f"Cantidad: {transaccion[2]}, Tipo: {transaccion[3]}, "
                              f"Precio Unitario: {transaccion[4]}, Acción: {transaccion[5]}, "
                              f"Símbolo: {transaccion[6]}, Estado: {transaccion[7]}")
                else:
                    print(f"No hay transacciones para el inversor con ID {id_usuario}")

        except self.connection.Error as e:
            print(f"Error al ejecutar la consulta: {e.args[0]}, {e.args[1]}")

    def obtener_operaciones_rendimiento(self,id_usuario):
        try:
            with self.connection.cursor() as cursor:
                consulta = """
                SELECT 
                    O.id_accion, A.nombre, A.simbolo, O.precio_unit AS precio_compra, O.cantidad
                FROM 
                    Operacion O
                JOIN 
                    Accion A ON O.id_accion = A.id_accion
                WHERE 
                    O.id_usuario = %s
                """
                cursor.execute(consulta, (id_usuario,))
                resultados = cursor.fetchall()

                acciones_totales_usuario=[]
                for resultado in resultados:
                    id_accion, nombre, simbolo, precio_compra, cantidad = resultado
                    accion = (id_accion, nombre, simbolo, precio_compra, cantidad)
                    acciones_totales_usuario.append(accion)
                return acciones_totales_usuario

        except self.connection.Error as e:
            print(f"Error al obtener las operaciones del usuario: {e}")
    
    def obtener_invertido_en_acciones_usuario(self,id_usuario):
        try:
            with self.connection.cursor() as cursor:
                query = """
                    SELECT COALESCE(SUM(o.cantidad * o.precio_unit), 0) AS total_acciones
                    FROM Operacion o
                    WHERE o.id_usuario = %s AND o.tipo = 'compra'
                """
                cursor.execute(query, (id_usuario,))
                total_acciones = cursor.fetchone()[0] or 0
                return total_acciones
                
        except self.connection.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


