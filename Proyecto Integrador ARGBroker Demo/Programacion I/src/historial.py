import pymysql

class Historial:
    def __init__(self, host, database, user, password):
        self.conexion = None
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conectar()

    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexión establecida con la base de datos.")
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e.args[0]}, {e.args[1]}")

    def obtener_historial_transacciones(self, id_usuario):
        try:
            with self.conexion.cursor() as cursor:
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

        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e.args[0]}, {e.args[1]}")

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    db = Historial(
        host="camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com",
        database="argbroker",
        user="admin",
        password="8xXnpE4d9BXXeheu2pWH"
    )

    try:
        id_usuario = int(input("Introduce el ID del inversor: "))
        db.obtener_historial_transacciones(id_usuario)
    except ValueError:
        print("El ID del inversor debe ser un número entero.")
    
    db.cerrar_conexion()
