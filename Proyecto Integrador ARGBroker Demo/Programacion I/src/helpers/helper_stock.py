from ..database.conexion_accion import ConexionDatabaseAccion
from ..database.conexion_movimiento import ConexionDatabaseMovimiento
from ..database.conexion_operacion import ConexionDatabaseOperacion
from ..helpers.helper_transaccion import HelperTransaccion
from ..helpers.validaciones import Validaciones

class HelperStock:
    def __init__(self,conexion_accion_db:ConexionDatabaseAccion,
                 helper_transaccion:HelperTransaccion,
                 validaciones:Validaciones,
                 conexion_movimiento_db:ConexionDatabaseMovimiento,
                 conexion_operacion_db:ConexionDatabaseOperacion):
        self.conexion_accion_db=conexion_accion_db
        self.helper_transaccion=helper_transaccion
        self.validaciones=validaciones
        self.conexion_movimiento_db=conexion_movimiento_db
        self.conexion_operacion_db=conexion_operacion_db

    def cantidad_total_acciones(self):
        print("Acciones Disponibles: ")
        cantidad_total_acciones= self.conexion_accion_db.get_all_acciones()
        self.helper_transaccion.mostrar_cantidad_total_acciones(cantidad_total_acciones)
        return cantidad_total_acciones

    def solicitar_accion_comprar(self, cantidad_total_acciones):
        accion_a_comprar = input("\nEscriba el símbolo de la acción que quiere comprar: ")
        if not self.validaciones.validacion_accion_simbolo_existe(cantidad_total_acciones, accion_a_comprar):
            return None
        return accion_a_comprar
    def obtener_precio_accion(self,accion):
        return self.conexion_movimiento_db.consultar_simbolo(accion)
    def confirmar_operacion(self):
        print("\nDesea continuar la operacion:")
        print("1. Si")
        print("2. No")
        continuar_operacion=input("Seleccione una opcion: ")
        return continuar_operacion == "1"
    
    def procesar_compra(self,cantidad_total_acciones,accion_a_comprar,usuario,precio_accion):
        cantidad_acciones=int(input(f"\nEscriba la cantidad de acciones de {accion_a_comprar} que desea adquirir: "))
        saldo_usuario=self.conexion_movimiento_db.calcular_saldo(usuario.get_id_usuario())

        saldo_total=self.calcular_saldo_total_compra(precio_accion,cantidad_acciones)

        if not self.validaciones.validacion_saldo_compra_acciones(saldo_usuario,saldo_total):
            print("No tienes saldo suficiente para realizar esta compra")
            return False
        
        id_accion_a_comprar=self.helper_transaccion.obtener_id_accion(cantidad_total_acciones,accion_a_comprar)

        self.ejecutar_compra(usuario, id_accion_a_comprar, cantidad_acciones, precio_accion)
    
    def calcular_saldo_total_compra(self, precio_accion, cantidad_acciones):
        saldo_a_abonar_por_compra = precio_accion * cantidad_acciones
        comision_broker = saldo_a_abonar_por_compra * 0.015
        return saldo_a_abonar_por_compra + comision_broker
    
    def ejecutar_compra(self,usuario,id,cantidad_acciones,precio_accion):
        print("Realizando compra ...")
        self.conexion_operacion_db.add_operacion(1,usuario.get_id_usuario(),id,cantidad_acciones,"compra",precio_accion)
        return False
