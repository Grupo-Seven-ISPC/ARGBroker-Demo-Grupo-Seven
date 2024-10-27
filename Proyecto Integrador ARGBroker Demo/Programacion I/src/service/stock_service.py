from ..helpers.helper_stock import HelperStock
from ..database.conexion_accion import ConexionDatabaseAccion
from ..database.conexion_cotizaciones import ConexionDatabaseCotizaciones
class StockService:
    def __init__(self,helper_stock:HelperStock):
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

    def venta_acciones(self,usuario):
        print("-------------------------------------")
        print("VENDER ACCIONES")
        print("-------------------------------------")
        acciones_usuario=self.helper_stock.cantidad_total_acciones_usuario_venta(usuario)
        accion_a_vender=self.helper_stock.solicitar_accion_vender(acciones_usuario)

        if not accion_a_vender:
            print("Accion Invalida")
            self.venta_acciones(usuario)

        precio_venta=self.helper_stock.obtener_precio_accion_venta(accion_a_vender)

        if not self.helper_stock.confirmar_operacion():
            return False
        self.helper_stock.procesar_venta(usuario,accion_a_vender,precio_venta) 

        

        
        
        