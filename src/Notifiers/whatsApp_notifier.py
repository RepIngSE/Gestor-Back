from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsappNotifier:
    def update(self, event: str, data: dict):
        message = f"🔔 Evento: {event.replace('_', ' ').title()}\n"
        message += f"Nombre: {data.get('name')}\n"
        message += f"Email: {data.get('email')}\n"
        message += f"Cedúla: {data.get('CC')}\n"

        self.send_whatsapp_message(message)

    def send_whatsapp_message(self, message: str):
        try:
            account_sid = os.getenv("TWILIO_ACCOUNT_SID")
            auth_token = os.getenv("TWILIO_AUTH_TOKEN")
            from_number = os.getenv("TWILIO_WHATSAPP_FROM")
            to_number = os.getenv("WHATSAPP_TO")

            client = Client(account_sid, auth_token)
            client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            print("📲 Mensaje de WhatsApp enviado correctamente.")
        except Exception as e:
            print(f"❌ Error al enviar mensaje de WhatsApp: {e}")
