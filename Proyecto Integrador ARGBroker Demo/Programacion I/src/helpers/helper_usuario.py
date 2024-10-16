from helpers import Validaciones

class UsuarioHelper():
    def __init__(self):
        self.validaciones=Validaciones()

    def ingresar_cuil(self):
        cuil = input("Ingrese su CUIL (11 dígitos): ")
        validacion_cuil= self.validaciones.validacion_cuil(cuil)
        if not validacion_cuil:
            print("Cuil Invalido . Debe contener exavtamente 11 dígitos")
            self.ingresar_cuil()
        elif isinstance(validacion_cuil,str):
            print(validacion_cuil)
            self.ingresar_cuil()
        else:
            return cuil
    def ingresar_nombre(self):
        nombre = input("Ingrese su nombre: ").strip()
        validacion_nombre=self.validaciones.validacion_nombre(nombre)
        if not validacion_nombre:
            print("El nombre debe contener solo letras.")
            self.ingresar_nombre()
        else:
            return nombre         
    def ingresar_apellido(self):
        apellido = input("Ingrese su apellido: ").strip()
        validacion_apellido= self.validaciones.validacion_apellido(apellido)
        if not validacion_apellido:
            print("El apellido debe contener solo letras.")
            self.ingresar_apellido()
        else:
            return apellido.lower()
    def ingresar_email(self,inicio_sesion=False):
        email = input("Ingrese su email: ")
        validacion_email=self.validaciones.validacion_email(email,inicio_sesion)
        if not validacion_email:
            print("Correo electrónico inválido. Asegúrate de usar un formato correcto (ejemplo: correo@dominio.com).")
            self.ingresar_email()
        elif isinstance(validacion_email,str):
            print(validacion_email)
            self.ingresar_email()
        else:
            return email
    def ingresar_contraseña(self):
        contraseña = input("Ingrese su contraseña (mínimo 8 caracteres, al menos una mayúscula y una minúscula): ")
        validacion_contraseña=self.validaciones.validacion_contraseña(contraseña)
        if not validacion_contraseña:
            print(validacion_contraseña)
            self.ingresar_contraseña()
        else:
            return contraseña
    def ingresar_perfil(self):
        print("Perfiles de Usuario: ")
        print("1. Agresivo")
        print("2. Medio")
        print("3. Conservador ")
        perfil = input("Ingrese el tipo de perfil de usuario: ")
        validacion_perfil=self.validaciones.validacion_perfil(perfil)
        if not validacion_perfil:
            print("Perfil Invalido. Por favor ingrese una opcion valida")
            self.ingresar_perfil()
        else:
            return perfil
            

