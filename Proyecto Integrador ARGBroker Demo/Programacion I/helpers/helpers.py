class IntentosContraseña:
    def __init__(self):
        self.intentos_contraseña = 0

    def incrementar(self):
        self.intentos_contraseña += 1

    def resetear(self):
        self.intentos_contraseña = 0

    def obtener_intentos(self):
        return self.intentos_contraseña

def buscar_usuario_por_mail(listaConUsuarios, emailABuscar):
    usuario_a_buscar=None
    for usuario in listaConUsuarios:
        if usuario.email == emailABuscar:
            usuario_a_buscar=usuario
            break
    return usuario_a_buscar
