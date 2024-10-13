import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Cargar las variables de entorno
load_dotenv()  # Asegúrate de que esta línea tenga paréntesis

email_sender = "argbrokergruposeven@gmail.com"
password = os.getenv("PASSWORD")  # Asegúrate de que 'PASSWORD' esté definido en tu archivo .env
email_reciver = "marialis1903@gmail.com"

# Comprobar si la contraseña se ha cargado correctamente
if password is None:
    raise ValueError("No se pudo cargar la contraseña desde el archivo .env")

# Aquí deberías generar o tener el token de recuperación
token = "tu_token_aqui"  # Reemplaza con el token real que quieras enviar
subject = "Ingresa y gana"
body = f"Ingresa aqui para ganar en este mismo instante un Iphone 16 pro max 512gb (color rosa) una coquita y un pebete"  # Agrega el token al cuerpo del mensaje

# Crear el mensaje
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

# Crear contexto SSL
context = ssl.create_default_context()

# Enviar el correo electrónico
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)  # Iniciar sesión
        smtp.sendmail(email_sender, email_reciver, em.as_string())  # Enviar el correo
        print("Correo enviado con éxito!")
except Exception as e:
    print(f"Ocurrió un error: {e}")
