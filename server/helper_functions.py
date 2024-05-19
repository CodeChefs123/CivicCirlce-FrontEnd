from server import *
import base64
import smtplib
from email.mime.text import MIMEText
from server import session


def encode(message: str) -> str:
    """
    Encode string for privacy and encryption.
    Args:
        message: The string to be encoded.
    Returns:
        The encoded string.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64encode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def decode(message: str) -> str:
    """
    Decode string for privacy and encryption.
    Args:
        message: The string to be decoded.
    Returns:
        The decoded string.
    """
    if not message:
        return ""
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64decode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def send_email(subject: str, email_to: str, body: str) -> None:
    """
    Send Emails for 2-factor authentication and other notifications.
    Args:
        subject: The subject of the email.
        email_to: The recipient's email address.
        body: The body of the email.
    Returns:
        None
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


def login_verification(user_type: str = "admin") -> bool:
    """
    Verify user login based on user type.
    Args:
        user_type: The type of user to be verified. Default is "admin".
    Returns:
        True if the user type matches the session user type, False otherwise.
    """
    return True if session.get("userType") == user_type else False
