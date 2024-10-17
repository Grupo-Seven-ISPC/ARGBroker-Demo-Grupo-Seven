import uuid
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

class Helper:
    def generar_token(self):
        token = str(uuid.uuid4())
        token_final=token[:6]
        return token_final
    def enviar_mail_recuperacion(self,email_reciver,token):
        load_dotenv()
        email_sender = "argbrokergruposeven@gmail.com"
        password = os.getenv("PASSWORD")
        if password is None:
            raise ValueError("No se pudo cargar la contraseña desde el archivo .env")
        subject = "Token para cambio de Contraseña"
        body = f"Tu token para cambiar tu contraseña es {token}"
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_reciver
        em["Subject"] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)  
                smtp.sendmail(email_sender, email_reciver, em.as_string()) 
                print("Correo enviado con éxito!")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    def intentos_inicio_sesion(self,login,inicio_sesion,usuario,dashboard,start_program):
        intentos=0
        max_intentos=3
        while intentos< max_intentos:
            usuario_activo = login()
            if usuario_activo:
                inicio_sesion=True
                if inicio_sesion:
                    usuario_sesion_iniciada=usuario.convertir_tupla_diccionario(usuario_activo)
                    dashboard(usuario_sesion_iniciada) 
                    break
            else:
                intentos+=1
                print(f"Credenciales incorrecta. Intento {intentos} de {max_intentos}.")
                if intentos == max_intentos:
                    print("Número máximo de intentos alcanzado. Volviendo al menú principal.")
                    start_program()


