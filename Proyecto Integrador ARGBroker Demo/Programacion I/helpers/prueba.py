from itsdangerous import URLSafeTimedSerializer

secret_key = "mi_clave_secreta_super_segura"
serializer = URLSafeTimedSerializer(secret_key)

def generar_token(correo_usuario):
    token = serializer.dumps(correo_usuario)
    return token

def enviar_correo_recuperacion(correo_usuario, token):
    enlace_recuperacion = f"http://miaplicacion.com/recuperar/%7Btoken%7D"
    print(f"Enviando correo a {correo_usuario}:")
    print(f"Enlace para recuperar contraseña: {enlace_recuperacion}")

correo_usuario = "usuario@ejemplo.com"
token = generar_token(correo_usuario)
enviar_correo_recuperacion(correo_usuario, token)

def verificar_token(token, max_age=3600):  # max_age = 3600 segundos (1 hora)
    try:
        correo_usuario = serializer.loads(token, max_age=max_age)
        return correo_usuario
    except:
        return None  # Token inválido o expirado

def recuperar_contrasena(token):
    correo_usuario = verificar_token(token)
    if correo_usuario:
        print(f"Token válido. El usuario es: {correo_usuario}")
        # Aquí mostrarías un formulario para que el usuario ingrese su nueva contraseña
    else:
        print("Token inválido o expirado")
        # Mostrar mensaje de error o redirigir a una página de error




        
def cambiar_contrasena(token, nueva_contrasena):
    correo_usuario = verificar_token(token)
    if correo_usuario:
        actualizar_contrasena(correo_usuario, nueva_contrasena)
        print("Contraseña actualizada con éxito")
    else:
        print("Token inválido o expirado")