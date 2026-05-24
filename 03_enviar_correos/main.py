import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo():
    # Configuración de credenciales
    # RECOMENDACIÓN: Usa variables de entorno o un archivo .env para no exponer contraseñas
    your_email = 'ejemplo@gmail.com'
    your_password = 'PASSWORD...' # Generada en Google
    recipient = 'ejemplo@mail.com'

    # Configuración del mensaje
    message = MIMEMultipart()
    message['From'] = your_email
    message['To'] = recipient
    message['Subject'] = 'Email de agradecimiento'

    body = 'Muchos gracias a todos por el apoyo!! Se agradece mucho <3'
    message.attach(MIMEText(body, 'plain'))

    try:
        # Conexión con el servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Inicio de sesión
        server.login(your_email, your_password)
        
        # Envío del mensaje
        server.sendmail(your_email, recipient, message.as_string())
        server.quit()
        
        print('Email enviado correctamente.')
        
    except Exception as e:
        print(f'Error al enviar el email: {e}')

if __name__ == "__main__":
    enviar_correo()