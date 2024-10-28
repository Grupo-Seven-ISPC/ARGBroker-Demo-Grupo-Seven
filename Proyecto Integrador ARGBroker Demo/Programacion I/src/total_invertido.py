def calcular_total_invertido(self, id_usuario):
    try:
        with self.connection.cursor() as cursor:
            # Obtener el total de ingresos
            query_ingresos = """
                SELECT COALESCE(SUM(monto), 0) AS total_ingresos 
                FROM Movimiento 
                WHERE id_usuario = %s AND monto > 0
            """
            cursor.execute(query_ingresos, (id_usuario,))
            total_ingresos = cursor.fetchone()[0]

            # Obtener el total de egresos
            query_egresos = """
                SELECT COALESCE(SUM(monto), 0) AS total_egresos 
                FROM Movimiento 
                WHERE id_usuario = %s AND monto < 0
            """
            cursor.execute(query_egresos, (id_usuario,))
            total_egresos = cursor.fetchone()[0]

            # Calcular el valor total de las acciones
            query_acciones = """
                SELECT COALESCE(SUM(o.cantidad * o.precio_unit), 0) AS total_acciones
                FROM Operacion o
                WHERE o.id_usuario = %s AND o.tipo = 'compra'
            """
            cursor.execute(query_acciones, (id_usuario,))
            total_acciones = cursor.fetchone()[0] or 0

            # Calcular el total invertido
            total_invertido = total_ingresos - abs(total_egresos) + total_acciones
            print(f"Total invertido del usuario {id_usuario}: $ {total_invertido}")
            return total_invertido
    except self.connection.Error as e:
        print(f"Error en la base de datos: {e}")
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return 0
