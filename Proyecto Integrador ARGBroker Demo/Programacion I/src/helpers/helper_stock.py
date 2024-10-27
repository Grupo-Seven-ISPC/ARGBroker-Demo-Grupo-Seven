from ..database.conexion_accion import ConexionDatabaseAccion
from ..database.conexion_movimiento import ConexionDatabaseMovimiento
from ..database.conexion_operacion import ConexionDatabaseOperacion
from ..database.conexion_cotizaciones import ConexionDatabaseCotizaciones
from ..helpers.helper_transaccion import HelperTransaccion
from ..helpers.validaciones import Validaciones

class HelperStock:
    def __init__(self,conexion_accion_db:ConexionDatabaseAccion,
                 helper_transaccion:HelperTransaccion,
                 validaciones:Validaciones,
                 conexion_movimiento_db:ConexionDatabaseMovimiento,
                 conexion_operacion_db:ConexionDatabaseOperacion,
                 conexion_cotizaciones_db:ConexionDatabaseCotizaciones):
        self.conexion_accion_db=conexion_accion_db
        self.helper_transaccion=helper_transaccion
        self.validaciones=validaciones
        self.conexion_movimiento_db=conexion_movimiento_db
        self.conexion_operacion_db=conexion_operacion_db
        self.conexion_cotizaciones_db=conexion_cotizaciones_db

# Funciones que ayudan a la compra de Acciones

    def cantidad_total_acciones(self):
        print("Acciones Disponibles: ")
        cantidad_total_acciones= self.conexion_accion_db.get_all_acciones()
        self.helper_transaccion.mostrar_cantidad_total_acciones(cantidad_total_acciones)
        return cantidad_total_acciones

    def solicitar_accion_comprar(self, cantidad_total_acciones):
        accion_a_comprar = input("\nEscriba el símbolo de la acción que quiere comprar: ").upper()
        if not self.validaciones.validacion_accion_simbolo_existe_compra(cantidad_total_acciones, accion_a_comprar):
            return None
        print(accion_a_comprar)
        return accion_a_comprar
    
    def obtener_precio_accion(self,accion):
        return self.conexion_cotizaciones_db.consultar_simbolo_compra(accion)
    def confirmar_operacion(self):
        print("\nDesea continuar la operacion:")
        print("1. Si")
        print("2. No")
        continuar_operacion=input("Seleccione una opcion: ")
        return continuar_operacion == "1"
    
    def procesar_compra(self,cantidad_total_acciones,accion_a_comprar,usuario,precio_accion):
        cantidad_acciones=int(input(f"\nEscriba la cantidad de acciones de {accion_a_comprar} que desea adquirir: "))

        cantidad_acciones_disponible=self.conexion_accion_db.get_cantidad_acciones_disponibles(accion_a_comprar)

        if not  self.validaciones.validacion_cantidad_acciones_disponible(cantidad_acciones,cantidad_acciones_disponible[0]):
            print("No hay suficientes acciones en el mercado para realizar tu inversion")
            return False

        saldo_usuario=self.conexion_movimiento_db.calcular_saldo(usuario.get_id_usuario())

        saldo_total=self.calcular_saldo_total_compra(precio_accion,cantidad_acciones)

        if not self.validaciones.validacion_saldo_compra_venta_acciones(saldo_usuario,saldo_total):
            print("No tienes saldo suficiente para realizar esta compra")
            return False
        
        id_accion_a_comprar=self.helper_transaccion.obtener_id_accion(cantidad_total_acciones,accion_a_comprar)

        self.ejecutar_compra(usuario, id_accion_a_comprar, cantidad_acciones, precio_accion,accion_a_comprar)
    
    def calcular_saldo_total_compra(self, precio_accion, cantidad_acciones):
        saldo_a_abonar_por_compra = precio_accion * cantidad_acciones
        comision_broker = saldo_a_abonar_por_compra * 0.015
        return saldo_a_abonar_por_compra + comision_broker
    
    def ejecutar_compra(self,usuario,id,cantidad_acciones,precio_accion,accion_a_comprar):
        print("Realizando compra ...")
        self.conexion_operacion_db.add_operacion(1,usuario.get_id_usuario(),id,cantidad_acciones,"compra",precio_accion)
        self.conexion_accion_db.disminuir_cantidad_acciones(cantidad_acciones,accion_a_comprar)
        return False

# Funciones o metodos que ayudan a la VENTA DE ACCIONES

    def cantidad_total_acciones_usuario_venta(self,usuario):
        print("Acciones Disponibles: ")
        acciones_usuario=self.conexion_accion_db.get_cantidad_acciones_adquiridas_usuario(usuario.get_id_usuario())
        for accion in acciones_usuario:
            print(f"Accion : {accion[0]} , En propiedad : {accion[1]}")
        return acciones_usuario
    
    def solicitar_accion_vender(self, cantidad_total_acciones):
        accion_a_vender = input("Seleccione la accion/simbolo a vender: ").upper()
        if not self.validaciones.validacion_accion_simbolo_existe_venta(cantidad_total_acciones, accion_a_vender):
            return None
        return accion_a_vender
    
    def obtener_precio_accion_venta(self,accion):
        return self.conexion_cotizaciones_db.consultar_simbolo_venta(accion)
    
    def procesar_venta(self,usuario,simbolo,precio_venta):
        cantidad_a_vender=int(input("Seleccione la cantidad de acciones a vender : "))
        cantidad_acciones_disponible=self.conexion_accion_db.get_cantidad_acciones_adquiridas_usuario_por_simbolo(usuario.get_id_usuario(),simbolo)
        if not  self.validaciones.validacion_cantidad_acciones_disponible(cantidad_a_vender,cantidad_acciones_disponible[2]):
            print("No posees tantas acciones para realizar esta venta")
            return False
        
        saldo_usuario=self.conexion_movimiento_db.calcular_saldo(usuario.get_id_usuario())
        saldo_total,comision_a_pagar_broker=self.calcular_saldo_total_venta(precio_venta,cantidad_a_vender)
        if not self.validaciones.validacion_saldo_compra_venta_acciones(saldo_usuario,comision_a_pagar_broker):
            print("No tienes saldo suficiente para realizar esta venta")
            return False
        id_accion_a_vender=cantidad_acciones_disponible[0]

        self.ejecutar_venta(usuario,id_accion_a_vender,cantidad_a_vender,precio_venta,cantidad_acciones_disponible[1])

    def calcular_saldo_total_venta(self, precio_venta, cantidad_a_vender):
        saldo_a_cobrar_por_venta = precio_venta * cantidad_a_vender
        comision_broker = saldo_a_cobrar_por_venta * 0.015
        saldo_a_cobrar_total_por_venta=saldo_a_cobrar_por_venta - comision_broker
        return (saldo_a_cobrar_total_por_venta,comision_broker)
    def ejecutar_venta(self,usuario,id_accion,cantidad_acciones,precio_accion,accion_a_vender):
        print("Realizando venta ...")
        self.conexion_operacion_db.add_operacion(1,usuario.get_id_usuario(),id_accion,cantidad_acciones,"venta",precio_accion)
        self.conexion_accion_db.aumentar_cantidad_acciones(cantidad_acciones,accion_a_vender)
        return False