from ..models.usuario import Usuario
from ..helpers.helper_programa import HelperPrograma
from ..service.auth_service import AuthService
from ..service.password_service import PasswordService
from ..service.stock_service import StockService
from ..service.user_service import UserService

class ProgramaService:
    def __init__(self,auth_service:AuthService,password_service:PasswordService,stock_service:StockService,user_service:UserService,helper_programa:HelperPrograma):
        self.__inicio_sesion=False
        self.__primera_vez_programa=True
        self.helper_programa=helper_programa
        self.auth_service=auth_service
        self.password_service=password_service
        self.stock_service=stock_service
        self.user_service=user_service
        
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
            self.user_service.registrar_ingreso(usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "3":
            self.user_service.registrar_egreso(usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "4":
            self.user_service.mostrar_precio_accion()
            self.dashboard(usuario)
        elif opcion_usuario == "5":
            if not self.user_service.gestionar_acciones(usuario):
                self.dashboard(usuario)

        elif opcion_usuario == "6":
            print("Cerrando sesión...")
            self.start_program()
        else:
            print("Opción no válida. Intente nuevamente.")
            self.start_program()
    
  