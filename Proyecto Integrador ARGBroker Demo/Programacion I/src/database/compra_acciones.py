def compra_acciones(self, id_accion, cantidad, precio_unit, db):
    # Verificar saldo del usuario
    costo_total = cantidad * precio_unit
    if self.saldo < costo_total:
        print("Saldo insuficiente para realizar la compra.")
        return False

    # Registrar la compra en la base de datos
    try:
        with db.conexion.cursor() as cursor:
            # Insertar la operación de compra en la tabla de Operacion
            consulta_operacion = """
            INSERT INTO Operacion (id_usuario, id_accion, cantidad, tipo, precio_unit, fecha)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(consulta_operacion, (self.id_usuario, id_accion, cantidad, 'compra', precio_unit))
            
            # Actualizar el saldo del usuario tras la compra
            self.saldo -= costo_total
            consulta_saldo = "UPDATE Usuario SET saldo = %s WHERE id_usuario = %s"
            cursor.execute(consulta_saldo, (self.saldo, self.id_usuario))
            
            # Actualizar la cantidad de acciones en el portafolio
            consulta_portafolio = """
            INSERT INTO Portafolio (id_usuario, id_accion, cantidad) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE cantidad = cantidad + VALUES(cantidad)
            """
            cursor.execute(consulta_portafolio, (self.id_usuario, id_accion, cantidad))

        db.conexion.commit()
        print("Compra realizada y portafolio actualizado correctamente.")
        return True

    except pymysql.MySQLError as e:
        db.conexion.rollback()
        print(f"Error al registrar la operación de compra: {e}")
        return False
