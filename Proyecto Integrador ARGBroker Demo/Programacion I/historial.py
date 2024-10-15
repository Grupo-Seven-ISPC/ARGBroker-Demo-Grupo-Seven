import pymysql

try:
    conexion = pymysql.connect(
        host="camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com",
        database="argbroker",
        user="admin",
        password="8xXnpE4d9BXXeheu2pWH"
    )
    
    def obtener_historial_transacciones(id_usuario):
        with conexion.cursor() as cursor:
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

            # Mostrar el historial
            if resultados:
                for transaccion in resultados:
                    print(f"ID Operación: {transaccion[0]}, Fecha: {transaccion[1]}, "
                          f"Cantidad: {transaccion[2]}, Tipo: {transaccion[3]}, "
                          f"Precio Unitario: {transaccion[4]}, Acción: {transaccion[5]}, "
                          f"Símbolo: {transaccion[6]}, Estado: {transaccion[7]}")
            else:
                print(f"No hay transacciones para el inversor con ID {id_usuario}")

    # Solicitar el ID del usuario
    id_usuario = int(input("Introduce el ID del inversor: "))
    obtener_historial_transacciones(id_usuario)

except pymysql.MySQLError as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")

finally:
    # Asegurarse de cerrar la conexión
    if conexion:
        conexion.close()
        print("Conexión cerrada.")
1
