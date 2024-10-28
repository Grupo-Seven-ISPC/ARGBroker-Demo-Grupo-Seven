from ..models.usuario import Usuario
from ..helpers.helper_programa import HelperPrograma
from ..service.auth_service import AuthService
from ..service.password_service import PasswordService
from ..service.stock_service import StockService
from ..service.user_service import UserService
from ..database.conexion_operacion import ConexionDatabaseOperacion
from ..database.conexion_cotizaciones import ConexionDatabaseCotizaciones

class ProgramaService:
    def __init__(self,auth_service:AuthService,password_service:PasswordService,stock_service:StockService,user_service:UserService,helper_programa:HelperPrograma, conexion_operacion_db:ConexionDatabaseOperacion,conexion_cotizaciones_db:ConexionDatabaseCotizaciones):
        self.__inicio_sesion=False
        self.__primera_vez_programa=True
        self.helper_programa=helper_programa
        self.auth_service=auth_service
        self.password_service=password_service
        self.stock_service=stock_service
        self.user_service=user_service
        self.conexion_operacion_db=conexion_operacion_db
        self.conexion_cotizaciones_db=conexion_cotizaciones_db

    def get_inicio_sesion(self):
        return self.__inicio_sesion
    def set_inicio_sesion(self,valor):
        self.__inicio_sesion=valor
    def get_primera_vez_programa(self):
        return self.__primera_vez_programa
    def set_primera_vez_programa(self,valor):
        self.__primera_vez_programa=valor

    def start_program(self):
        opcion = self.helper_programa.opciones_programa_principal(self.get_primera_vez_programa,self.set_primera_vez_programa)
        if opcion == "1":
            self.register()
        elif opcion == "2":
           self.login()
        elif opcion == "3":
            respuesta=self.password_service.forgot_password()
            if respuesta :
                self.start_program()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            print("Opción no válida. Intente nuevamente.")

    def login(self):
        usuario=self.auth_service.login()
        if usuario:
            usuario_activo=Usuario.convertir_tupla_diccionario(usuario)
            self.dashboard(usuario_activo)
        else:
            print("Inicio de sesión fallido.")
           
    def register(self):
       if self.auth_service.register():
           self.start_program()

    def dashboard(self,usuario):
        opcion_usuario=self.helper_programa.opciones_dashboard()
        if opcion_usuario == "1":
            self.user_service.ver_saldo(usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "2":
            #Agregar al helper programa una funcion que haga esto y ademas muestre un print
            self.conexion_operacion_db.obtener_historial_transacciones(usuario.get_id_usuario())
            self.dashboard(usuario)
        elif opcion_usuario == "3":
            print("1. Rendimiento por Accion ")
            print("2. Rendimiento Total ")
            opcion= input("Seleccione una opcion: ")
            if opcion == "1":
                acciones_totales_usuario=self.conexion_operacion_db.obtener_operaciones_rendimiento(usuario.get_id_usuario())
                for accion in acciones_totales_usuario:
                    precio_actual=self.conexion_cotizaciones_db.consultar_simbolo_venta(accion[2])
                    rendimiento=self.calcular_rendimiento(precio_actual,accion[3])
                    if rendimiento is not None:
                        print(f"---\nAcción: {accion[1]} ({accion[2]})")
                        print(f"Precio de compra: {accion[3]}, Precio actual: {precio_actual}")
                        print(f"Rendimiento: {rendimiento:.2f}%")
                    else:
                        print(f"Precio actual no disponible para la acción {accion[1]}")
                self.dashboard(usuario)
            elif opcion == "2":
                pass
            else:
                print("Opcion Invalida")
                self.dashboard(usuario)
        elif opcion_usuario == "4":
            self.user_service.registrar_ingreso(usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "5":
            self.user_service.registrar_egreso(usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "6":
            self.user_service.mostrar_precio_accion()
            self.dashboard(usuario)
        elif opcion_usuario == "7":
            if not self.user_service.gestionar_acciones(usuario):
                self.dashboard(usuario)

        elif opcion_usuario == "8":
            print("Cerrando sesión...")
            self.start_program()
        else:
            print("Opción no válida. Intente nuevamente.")
            self.start_program()
    
    def calcular_rendimiento(self,precio_actual,precio_compra):
        if precio_actual > 0:
            rendimiento = ((precio_actual - precio_compra) / precio_compra) * 100
            return rendimiento
        else:
            return None