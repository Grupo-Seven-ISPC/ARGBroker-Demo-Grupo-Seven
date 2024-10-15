import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Cargar las variables de entorno
  # Asegúrate de que esta línea tenga paréntesis

def enviar_mail_recuperacion(email_reciver,token):
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


