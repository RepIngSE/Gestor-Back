import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()  

class EmailNotifier:
    def update(self, event: str, data: dict):
        subject = f"Notificación: {event.replace('_', ' ').title()}"
        body = f"Datos del usuario: {data}"

        # Correo del destinatario: puede ser dinámico
        to = os.getenv("NOTIFY_EMAIL", "admin@example.com")
        self.send_email(to, subject, body)

    def send_email(self, to, subject, body):

        # Datos desde .env
        from_address = os.getenv("EMAIL_FROM")
        password = os.getenv("EMAIL_PASSWORD")
        smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", 465))
        # Configura tu servidor SMTP (esto es un ejemplo básico con Gmail)

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_address
        msg["To"] = to

        try:
            with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
                server.login(from_address, password)
                server.send_message(msg)
                print("📧 Correo enviado exitosamente.")
        except Exception as e:
            print(f"❌ Error al enviar correo: {e}")
