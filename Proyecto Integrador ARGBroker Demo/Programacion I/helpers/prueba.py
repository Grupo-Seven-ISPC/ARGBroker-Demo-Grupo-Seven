from itsdangerous import URLSafeTimedSerializer
from helpers.envio import enviar_mail_recuperacion
import uuid

secret_key = "mi_clave_secreta_super_segura"
serializer = URLSafeTimedSerializer(secret_key)

def generar_token():
    token = str(uuid.uuid4())
    token_final=token[:6]
    return token_final

def prueba():
    token=generar_token()
    enviar_mail_recuperacion("fabri.avila3@gmail.com",token)
    toke_puto=input("Coloca el token correcto: ")
    if token == toke_puto:
        print("Perfecto token igual")
    else:
        print("Incorrecto")


