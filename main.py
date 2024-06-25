import smtplib, ssl
from db import get_expired_subscription_clients
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

# SMTP SERVER SETTINGS
port = int(os.getenv("PORT"))
smtp_server = os.getenv("SMTP_SERVER")

# ENTER SENDER EMAIL
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("APP_PASSWORD")

message = f"""\
Subject: Your subscription expired

Today {date.today()} we hierby announce that your subscription has expired. 
If you wish to continue using our service contact us at {sender_email}"""

# CONNECTION SMTP

with smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context()) as server:
    server.login(sender_email, password)

    # DATABASE CONNECT
    clients = get_expired_subscription_clients()

    # EMAIL SENDING
    for client in clients:
        print(f"Emails sent to: {client[3]}")
        try:
            server.sendmail(sender_email, client[3], message)
        except smtplib.SMTPException as error:
            print(f"Failed to send email: {error}")
        except Exception as unknown:
            print(f"Unknwon error: {unknown}")

