from ..helpers.helper_stock import HelperStock

class StockService:
    def __init__(self,helper_stock=HelperStock):
        self.helper_stock=helper_stock

    def compra_acciones(self,usuario):
        print("-------------------------------------")
        print("COMPRAR ACCIONES")
        print("-------------------------------------")
        
        cantidad_total_acciones= self.helper_stock.cantidad_total_acciones()

        accion_a_comprar= self.helper_stock.solicitar_accion_comprar(cantidad_total_acciones)

        if not accion_a_comprar:
            print("Accion Invalida")
            self.compra_acciones(usuario)
        
        precio_accion=self.helper_stock.obtener_precio_accion(accion_a_comprar)

        if not self.helper_stock.confirmar_operacion():
            return False
        self.helper_stock.procesar_compra(cantidad_total_acciones,accion_a_comprar,usuario,precio_accion)

    def venta_acciones(self):
        print("-------------------------------------")
        print("VENDER ACCIONES")
        print("-------------------------------------")
        print("Acciones Disponibles: ")