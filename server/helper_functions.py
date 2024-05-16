from server import *


def encode(message: str) -> bytes:
    """
    Encode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64encode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def decode(message: str) -> bytes:
    """
    Decode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64decode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def send_email(subject: str, email_to: str, body: str) -> None:
    """
    Send Emails for 2 fac auth and other notifications
    """
    EmailAdd = "circlecivic@gmail.com"
    Pass = "civiccirclemindstudiociac"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = EmailAdd
    msg["To"] = email_to
    try:
        s = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
        s.login(user=EmailAdd, password=Pass)
        s.sendmail(EmailAdd, email_to, msg.as_string())
        s.quit()
    except:
        server = smtplib.SMTP_SSL("smtp.googlemail.com", 465)
        server.login(EmailAdd, Pass)
        server.sendemail(EmailAdd, email_to, msg.as_string())
