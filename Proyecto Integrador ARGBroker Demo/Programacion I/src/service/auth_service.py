from ..helpers.helper_usuario import HelperUsuario
from ..database.conexion_usuario import ConexionDatabaseUsuario
from ..database.conexion_movimiento import ConexionDatabaseMovimiento
from ..models.usuario import Usuario

class AuthService:
    def __init__(self,helper_usuario:HelperUsuario , conexion_usuario_db:ConexionDatabaseUsuario, conexion_movimiento_db:ConexionDatabaseMovimiento):
        self.helper_usuario=helper_usuario
        self.conexion_usuario_db=conexion_usuario_db
        self.conexion_movimiento_db=conexion_movimiento_db

    def login(self):
        print("\nFormulario de Inicio de Sesión:")
        intentos=0
        max_intentos=3
        while intentos< max_intentos:
            email=self.helper_usuario.ingresar_email(inicio_sesion=True)
            contraseña=self.helper_usuario.ingresar_contraseña()
            email_encontrado= self.conexion_usuario_db.get_one({"email":email,"contraseña":contraseña})
            if email_encontrado :
                return email_encontrado
            else:
                intentos +=1
                print(f"Credenciales incorrecta. Intento {intentos} de {max_intentos}.")
                if intentos == max_intentos:
                    print("Número máximo de intentos alcanzado. Volviendo al menú principal.")
                    return False
    
    def register(self):
        cuil=self.helper_usuario.ingresar_cuil()
        nombre = self.helper_usuario.ingresar_nombre()
        apellido= self.helper_usuario.ingresar_apellido()
        email=self.helper_usuario.ingresar_email()
        contraseña=self.helper_usuario.ingresar_contraseña()
        perfil=self.helper_usuario.ingresar_perfil()

        usuario_final=Usuario(0, cuil, nombre, apellido, email, contraseña, perfil)

        id_usuario=self.conexion_usuario_db.add(usuario_final)

        self.conexion_movimiento_db.registrar_ingreso(1000000,id_usuario,mensaje="Monto Inicial/Apertura de Cuenta")
        
        return True
