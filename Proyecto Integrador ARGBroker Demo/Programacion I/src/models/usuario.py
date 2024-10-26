class Usuario:
    def __init__(self, id_usuario,cuil, nombre, apellido, email, contraseña,perfil):
        self.__id_usuario=id_usuario
        self.__cuil = cuil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contraseña = contraseña
        self.__perfil=perfil
        
    def get_id_usuario(self):
        return self.__id_usuario
    def set_id_usuario(self,valor):
        self.__id_usuario=valor
        
    def get_cuil(self):
        return self.__cuil
    def set_cuil(self,valor):
        self.__cuil=valor

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,valor):
        self.__nombre=valor

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,valor):
        self.__apellido=valor

    def get_email(self):
        return self.__email
    def set_email(self,valor):
        self.__email=valor

    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self,valor):
        self.__contraseña=valor

    def get_perfil(self):
        return self.__perfil
    def set_perfil(self,valor):
        self.__perfil=valor
        
    @classmethod
    def convertir_tupla_diccionario(objeto, datos):
        id_usuario, cuil, nombre, apellido, email, perfil, contraseña = datos
        return objeto(id_usuario, cuil, nombre, apellido, email, contraseña, perfil)