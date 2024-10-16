from models import Usuario
from helpers import UsuarioHelper
from helpers import Helper
from helpers import Validaciones
from database import ConexionDatabaseUsuario
from database import ConexionDatabaseMovimiento

class ProgramaPrincipal:
    def __init__(self,conexion_usuario_db=ConexionDatabaseUsuario(),conexion_movimiento_db=ConexionDatabaseMovimiento(),usuario_helper=UsuarioHelper(),helper=Helper(),validaciones=Validaciones()):
        self.inicio_sesion=False
        self.usuario_helper=usuario_helper
        self.helper=helper
        self.validaciones=validaciones
        self.conexion_usuario_db=conexion_usuario_db
        self.conexion_movimiento_db=conexion_movimiento_db
        self.primera_vez_programa=True
        
    def __str__(self):
        pass
    
    def start_program(self):
        if self.primera_vez_programa:
            print("Bienvenido al sistema.")
            self.primera_vez_programa=False
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Olvido su contraseña?")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.register()
        elif opcion == "2":
            intentos=0
            max_intentos=3
            while intentos< max_intentos:
                usuario_activo = self.login()
                if usuario_activo:
                    self.inicio_sesion=True
                    if self.inicio_sesion:
                        usuario_sesion_iniciada=Usuario.convertir_tupla_diccionario(usuario_activo)
                        self.dashboard(usuario_sesion_iniciada) 
                        break
                else:
                    intentos+=1
                    print(f"Credenciales incorrecta. Intento {intentos} de {max_intentos}.")
                    if intentos == max_intentos:
                        print("Número máximo de intentos alcanzado. Volviendo al menú principal.")
                        self.start_program()
            
        elif opcion == "3":
            self.forgot_password()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            return
        else:
            print("Opción no válida. Intente nuevamente.")

    def login(self):
        print("\nFormulario de Inicio de Sesión:")
        email=self.usuario_helper.ingresar_email(inicio_sesion=True)
        contraseña=self.usuario_helper.ingresar_contraseña()
        email_encontrado= self.conexion_usuario_db.get_one({"email":email,"contraseña":contraseña})
        return email_encontrado if email_encontrado else False
    
    def register(self):
        cuil=self.usuario_helper.ingresar_cuil()
        nombre = self.usuario_helper.ingresar_nombre()
        apellido= self.usuario_helper.ingresar_apellido()
        email=self.usuario_helper.ingresar_email()
        contraseña=self.usuario_helper.ingresar_contraseña()
        perfil=self.usuario_helper.ingresar_perfil()

        usuario_final=Usuario(0, cuil, nombre, apellido, email, contraseña, perfil)

        id_usuario=self.conexion_usuario_db.add(usuario_final)

        self.conexion_movimiento_db.registrar_ingreso(1000000,id_usuario,mensaje="Monto Inicial/Apertura de Cuenta")
        self.start_program()

    def forgot_password(self):
        print("\n¿Has olvidado tu contraseña?")
        print("\n1. Reestablecer Contraseña")
        print("\n2. Volver a iniciar sesion")
        contraseña_olvidada= input("\nSeleccione una opcion: ")
        if contraseña_olvidada == "1":
            email= input("Ingrese el email con el cual esta asociado su cuenta : ")
            usuario_a_buscar=self.conexion_usuario_db.get_one({"email":email})
            if usuario_a_buscar:
                print("Usuario encontrado exitosamente")
                print("Se esta enviando a tu correo electronico el token para el cambio de contraseña.Aguarde unos instantes .....")
                token_usuario=self.helper.generar_token()
                self.helper.enviar_mail_recuperacion(email,token_usuario)
                token_confirmacion=input("Ingrese el token de seguridad: ")
                if token_usuario == token_confirmacion:
                    contraseña_nueva=input("Ingrese la nueva contraseña :")
                    validar_contraseña=self.validaciones.validacion_contraseña(contraseña_nueva)
                    if not validar_contraseña:
                        print("Contraseña con formato inadecuado")
                        return
                    contraseña_nueva_repetida=input("Ingrese la nueva contraseña de nuevo :")
                    validar_contraseña_repetida= self.validaciones.validacion_contraseña(contraseña_nueva_repetida)
                    if not validar_contraseña_repetida:
                        print("Contraseña con formato inadecuado")
                        return
                    if contraseña_nueva == contraseña_nueva_repetida:
                        self.conexion_usuario_db.update("contraseña",contraseña_nueva,"email",email)
                        print("Contraseña cambiada correctamente")
                        self.start_program()
                    else:
                        print("Las contraseñas no coinciden")
                        return
                        
                else:
                    print("Codigo de verificacion incorrecto")
                    return
            
            else:
                print("No se encontro al usuario con ese email")
                return
        elif contraseña_olvidada == "2":
            self.login()
        else:
            print("Opción no válida. Intente nuevamente.")
            self.forgot_password()

    def dashboard(self,usuario):
        print("\n1. Ver saldo actual")
        print("2. Registrar ingreso")
        print("3. Registrar egreso")
        print("4. Cerrar sesión")
        opcion_usuario = input("Seleccione una opción: ")
        if opcion_usuario == "1":
            print(f"Saldo actual: ${self.conexion_movimiento_db.calcular_saldo(usuario.id_usuario)}")
            self.dashboard(usuario)
        elif opcion_usuario == "2":
            monto = float(input("Ingrese el monto del ingreso: "))
            self.conexion_movimiento_db.registrar_ingreso(monto,usuario.id_usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "3":
            monto = float(input("Ingrese el monto del egreso: "))
            self.conexion_movimiento_db.registrar_egreso(monto,usuario.id_usuario)
            self.dashboard(usuario)
        elif opcion_usuario == "4":
            print("Cerrando sesión...")
            self.start_program()
        else:
            print("Opción no válida. Intente nuevamente.")
            self.start_program()