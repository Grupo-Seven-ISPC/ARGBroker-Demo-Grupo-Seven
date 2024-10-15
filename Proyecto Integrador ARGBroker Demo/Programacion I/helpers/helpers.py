class IntentosContraseña:
    def __init__(self):
        self.intentos_contraseña = 0

    def incrementar(self):
        self.intentos_contraseña += 1

    def resetear(self):
        self.intentos_contraseña = 0

    def obtener_intentos(self):
        return self.intentos_contraseña

def buscar_usuario_por_mail(connection,emailABuscar):
    cursor = connection.cursor()
    insert_query= """
        SELECT email FROM Usuarios WHERE email = %s
    """
    values=(emailABuscar,)
    cursor.execute(insert_query,values)
    email_usuario_buscado= cursor.fetchall()
    if len(email_usuario_buscado) >=1:
        return email_usuario_buscado[0][0]
    else:
        return None

def cambiar_contraseña_bd(connection,nuevaContraseña,email):
    cursor = connection.cursor()
    insert_query= """
        UPDATE Usuarios SET contraseña = %s WHERE email = %s
    """
    values=(nuevaContraseña,email)
    cursor.execute(insert_query,values)
    cursor.fetchall()