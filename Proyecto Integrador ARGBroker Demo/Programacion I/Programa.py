from Connection import ConexionDatabase
from Usuario import Usuario
from HelperUsuario import UsuarioHelper
from Helper import Helper
from Validaciones import Validaciones

class ProgramaPrincipal():
    def __init__(self):
        self.inicio_sesion=False
        self.usuario_helper=UsuarioHelper()
        self.conexion_database=ConexionDatabase()
        
    def __str__(self):
        pass
    
    def start_program(self):
        print("Bienvenido al sistema.")
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Olvido su contraseña?")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.register()
        elif opcion == "2":
            usuario_activo = self.login()
            if usuario_activo:
                self.inicio_sesion=True
            if self.inicio_sesion:
                    usuario_sesion_iniciada=Usuario.convertir_tupla_diccionario(usuario_activo)
                    self.dashboard(usuario_sesion_iniciada,self.conexion_database.get_connection())
        elif opcion == "3":
            self.forgot_password()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            return
        else:
            print("Opción no válida. Intente nuevamente.")

    def login(self):
        print("\nFormulario de Inicio de Sesión:")
        email=self.usuario_helper.ingresar_email()
        contraseña=self.usuario_helper.ingresar_contraseña()
        columnas=["email","contraseña"]
        email_encontrado= self.conexion_database.search_one_in_database("Usuarios",columnas,(email,contraseña))
        return email_encontrado if email_encontrado else False
    
    def register(self):
        cuil=self.usuario_helper.ingresar_cuil()
        nombre = self.usuario_helper.ingresar_nombre()
        apellido= self.usuario_helper.ingresar_apellido()
        email=self.usuario_helper.ingresar_email()
        contraseña=self.usuario_helper.ingresar_contraseña()
        perfil=self.usuario_helper.ingresar_perfil()
        usuario_final=Usuario(0, cuil, nombre, apellido, email, contraseña, perfil)
        self.conexion_database.add_to_database("Usuarios",usuario_final)
        self.start_program()

    def forgot_password(self):
        print("\n¿Has olvidado tu contraseña?")
        print("\n1. Reestablecer Contraseña")
        print("\n2. Volver a iniciar sesion")
        contraseña_olvidada= input("\nSeleccione una opcion: ")
        if contraseña_olvidada == "1":
            email= input("Ingrese el email con el cual esta asociado su cuenta : ")
            usuario_a_buscar=ConexionDatabase.search_one_in_database("Usuarios","email",email)
            if usuario_a_buscar:
                print("Usuario encontrado exitosamente")
                print("Se esta enviando a tu correo electronico el token para el cambio de contraseña.Aguarde unos instantes .....")
                token_usuario=Helper.generar_token()
                Helper.enviar_mail_recuperacion(email,token_usuario)
                token_confirmacion=input("Ingrese el token de seguridad: ")
                if token_usuario == token_confirmacion:
                    contraseña_nueva=input("Ingrese la nueva contraseña :")
                    validar_contraseña=Validaciones.validacion_contraseña(contraseña_nueva)
                    if not validar_contraseña:
                        print("Contraseña con formato inadecuado")
                        return
                    contraseña_nueva_repetida=input("Ingrese la nueva contraseña de nuevo :")
                    validar_contraseña_repetida= Validaciones.validacion_contraseña(contraseña_nueva_repetida)
                    if not validar_contraseña_repetida:
                        print("Contraseña con formato inadecuado")
                        return
                    if contraseña_nueva == contraseña_nueva_repetida:
                        ConexionDatabase.update_one_column("Usuarios","contraseña",contraseña_nueva,"email",email)
                        print("Contraseña cambiada correctamente")
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

    def dashboard(self,usuario,conexion):
        print("\n1. Ver saldo actual")
        print("2. Registrar ingreso")
        print("3. Registrar egreso")
        print("4. Cerrar sesión")
        opcion_usuario = input("Seleccione una opción: ")
        if opcion_usuario == "1":
            print(f"Saldo actual: ${usuario.calcular_saldo(conexion)}")
        elif opcion_usuario == "2":
            monto = float(input("Ingrese el monto del ingreso: "))
            usuario.registrar_ingreso(monto)
        elif opcion_usuario == "3":
            monto = float(input("Ingrese el monto del egreso: "))
            usuario.registrar_egreso(monto)
        elif opcion_usuario == "4":
            print("Cerrando sesión...")
            self.start_program()
        else:
            print("Opción no válida. Intente nuevamente.")
            self.start_program()