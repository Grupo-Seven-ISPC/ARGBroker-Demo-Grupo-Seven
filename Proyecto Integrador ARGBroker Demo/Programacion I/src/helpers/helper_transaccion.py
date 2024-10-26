class HelperTransaccion:
    def __init__(self):
        pass
    def obtener_id_accion(self,listado_acciones,accion):
        for accion_individual in listado_acciones:
            if accion == accion_individual[2]:
                return accion_individual[0]
    def mostrar_cantidad_total_acciones(self,acciones):
        for accion in acciones:
            print(f"Empresa : {accion[1]} , Simbolo : {accion[2]}, Cantidad : {accion[3]}")