class Usuario:
    def __init__(self, id_usuario,cuil, nombre, apellido, email, contraseña,perfil):
        self.id_usuario=id_usuario
        self.cuil = cuil
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.perfil=perfil
        
    @classmethod
    def convertir_tupla_diccionario(objeto, datos):
        id_usuario, cuil, nombre, apellido, email, perfil, contraseña = datos
        return objeto(id_usuario, cuil, nombre, apellido, email, contraseña, perfil)

    def registrar_inversion():
        pass
    def gestionar_perfil():
        pass