import re
from ..database.conexion_usuario import ConexionDatabaseUsuario

class Validaciones:
    def __init__(self,conexion_usuario_db:ConexionDatabaseUsuario):
        self.conexion_usuario_db=conexion_usuario_db

    def validacion_cuil(self,cuil):
        if len(cuil) == 11 and cuil.isdigit():
            cuil_existe=self.conexion_usuario_db.get_one({"cuil":cuil})
            if cuil_existe:
                return "CUIL ya registrado. Intente con otro."
            return  True
        else:
            return False
    def validacion_nombre(self,nombre):
        if nombre.isalpha():
            return True
        else :
            return False
    def validacion_apellido(self,apellido):
        if apellido.isalpha():
            return True
        else :
            return False
    def validacion_email(self,email,inicio_sesion=False):
         if re.match(r'^[\w\.-]+@(gmail\.com|hotmail\.com|yahoo\.com)$', email):
             email_existe=self.conexion_usuario_db.get_one({"email":email})
             if email_existe and inicio_sesion == False:
                return "El email ya está registrado. Intente con otro."
             return True
         else:
             return False
    def validacion_contraseña(self,contraseña):
        if len(contraseña) < 8:
            return"La contraseña debe tener al menos 8 caracteres."
        elif not re.search("[A-Z]", contraseña):
            return"La contraseña debe contener al menos una letra mayúscula."
        elif not re.search("[a-z]", contraseña):
            return"La contraseña debe contener al menos una letra minúscula."
        else:
            return True
    def validacion_perfil(self,perfil):
        if perfil == "1" or perfil == "2" or perfil == "3" :
            return True
        else:
            return False
    def validacion_accion_simbolo_existe_compra(self,listado_acciones,simbolo):
        existe_accion=False
        for accion in listado_acciones:
            if simbolo == accion[2]:
                existe_accion= True
        return existe_accion
    def validacion_saldo_compra_venta_acciones(self,saldo_total,saldo_a_abonar):
        if saldo_total - saldo_a_abonar >=0:
            return True
        else :
            return False
    def validacion_cantidad_acciones_disponible(self,cantidad_acciones_a_comprar,cantidad_disponible):
        if (cantidad_disponible - cantidad_acciones_a_comprar)>=0:
            return True
        else:
            return False 
    def validacion_accion_simbolo_existe_venta(self,listado_acciones,simbolo):
        existe_accion=False
        for accion in listado_acciones:
            if simbolo == accion[0]:
                existe_accion= True
        return existe_accion