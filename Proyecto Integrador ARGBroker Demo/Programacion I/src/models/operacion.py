class Operacion:
    def __init__(self,id_operacion,fecha,id_estado,id_usuario,id_accion,cantidad,tipo,precio_unit):
        self.id_operacion=id_operacion
        self.fecha=fecha
        self.id_estado=id_estado
        self.id_usuario=id_usuario
        self.id_accion=id_accion
        self.cantidad=cantidad
        self.tipo=tipo
        self.precio_unit=precio_unit

    # Posiblemente la eliminemos por que no la necesitamos