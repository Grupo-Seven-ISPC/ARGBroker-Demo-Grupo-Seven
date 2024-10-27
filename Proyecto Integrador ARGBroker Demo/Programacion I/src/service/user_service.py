from ..database.conexion_movimiento import ConexionDatabaseMovimiento
from ..database.conexion_cotizaciones import ConexionDatabaseCotizaciones
from .stock_service import StockService

class UserService:
    def __init__(self, conexion_movimiento_db:ConexionDatabaseMovimiento, stock_service:StockService,conexion_cotizaciones_db: ConexionDatabaseCotizaciones):
        self.conexion_movimiento_db = conexion_movimiento_db
        self.stock_service = stock_service
        self.conexion_cotizaciones_db=conexion_cotizaciones_db

    def ver_saldo(self, usuario):
        saldo = self.conexion_movimiento_db.calcular_saldo(usuario.get_id_usuario())
        print(f"Saldo actual: ${saldo}")

    def registrar_ingreso(self, usuario):
        monto = float(input("Ingrese el monto del ingreso: "))
        self.conexion_movimiento_db.registrar_ingreso(monto, usuario.get_id_usuario())

    def registrar_egreso(self, usuario):
        monto = float(input("Ingrese el monto del egreso: "))
        self.conexion_movimiento_db.registrar_egreso(monto, usuario.get_id_usuario())

    def mostrar_precio_accion(self):
        simbolo = input("Seleccione el símbolo de la acción a consultar: ")
        precio_compra = self.conexion_cotizaciones_db.consultar_simbolo_compra(simbolo)
        precio_venta = self.conexion_cotizaciones_db.consultar_simbolo_venta(simbolo)
        print(f"El precio actual de {simbolo} para compra es: ${precio_compra} y para la venta es : ${precio_venta}")

    def gestionar_acciones(self, usuario):
        print("1. Comprar Acciones")
        print("2. Vender Acciones")
        opcion_usuario_accion = input("Seleccione la opción: ")
        if opcion_usuario_accion == "1":
            self.stock_service.compra_acciones(usuario)
        elif opcion_usuario_accion == "2":
            self.stock_service.venta_acciones(usuario)
        else:
            print("Opción no válida. Intente nuevamente.")
            return False
