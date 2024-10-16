import re


class Validaciones():
    def __str__(self):
        pass

    def validacion_cuil(self,cuil):
        if len(cuil) == 11 and cuil.isdigit():
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
    def validacion_email(self,email):
         if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
             return True
         else:
             return False
    def validacion_contraseña(self,contraseña):
        if len(contraseña) < 8 or not re.search("[A-Z]", contraseña) or not re.search("[a-z]", contraseña):
            return False
        else:
            return True
    def validacion_perfil(self,perfil):
        if perfil == "1" or perfil == "2" or perfil == "3" :
            return True
        else:
            return False