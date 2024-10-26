from ..database.conexion_usuario import ConexionDatabaseUsuario
from ..helpers.helper_password import HelperPassword
from ..helpers.validaciones import Validaciones
from ..service.auth_service import AuthService

class PasswordService:
    def __init__(self,conexion_usuario_db:ConexionDatabaseUsuario,helper_password:HelperPassword,validaciones:Validaciones,auth_service:AuthService):
        self.conexion_usuario_db=conexion_usuario_db
        self.helper_password=helper_password
        self.validaciones=validaciones
        self.auth_service=auth_service

    def forgot_password(self):
        print("\n¿Has olvidado tu contraseña?")
        print("\n1. Reestablecer Contraseña")
        print("\n2. Volver a iniciar sesion")
        while True:
            contraseña_olvidada= input("\nSeleccione una opcion: ")
            if contraseña_olvidada == "1":
                if self._reset_password():
                    return True
                break
            elif contraseña_olvidada == "2":
                self.auth_service.login()
            else:
                print("Opción no válida. Intente nuevamente.")

    def _reset_password(self):
        email= input("Ingrese el email con el cual esta asociado su cuenta : ")
        usuario_a_buscar=self.conexion_usuario_db.get_one({"email":email})

        if usuario_a_buscar:
            print("Usuario encontrado exitosamente")
            print("Se esta enviando a tu correo electronico el token para el cambio de contraseña.Aguarde unos instantes .....")

            token_usuario=self.helper_password.generar_token()
            self.helper_password.enviar_mail_recuperacion(email,token_usuario)
            token_confirmacion=input("Ingrese el token de seguridad: ")

            if token_usuario == token_confirmacion:
                if self._confirmar_contraseña_nueva(email):
                    return True
            else:
                print("Codigo de verificacion incorrecto")
        else:
            print("No se encontro al usuario con ese email")

    def _confirmar_contraseña_nueva(self,email):
        while True:
            contraseña_nueva=input("Ingrese la nueva contraseña :")

            validacion_contraseña=self.validaciones.validacion_contraseña(contraseña_nueva)
            if validacion_contraseña != True:
                print("Contraseña con formato inadecuado")
                print(validacion_contraseña)
                continue

            contraseña_nueva_repetida=input("Ingrese la nueva contraseña de nuevo :")
            if contraseña_nueva != contraseña_nueva_repetida: 
                print("Las contraseñas no coinciden")
                continue

            validacion_contraseña_repetida=self.validaciones.validacion_contraseña(contraseña_nueva_repetida)
            if validacion_contraseña_repetida != True:
                print("Contraseña con formato inadecuado")
                print(validacion_contraseña_repetida)
                continue
                    
            self.conexion_usuario_db.update("contraseña",contraseña_nueva,"email",email)
            print("Contraseña cambiada correctamente")
            return True
               
                