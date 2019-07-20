import smtplib
from email.message import EmailMessage
import reddit_post


def send_email(email):

    EMAIL_ADDRESS = "yvann.jeral12@outlook.com"
    EMAIL_PASSWORD = "Yrdenciri123"

    msg = EmailMessage()
    msg["Subject"] = "r_OnePiece_Project"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content("Testing stuff")

    msg.add_alternative(email, subtype="html")

    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

