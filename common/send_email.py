
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = "yvann.jeral12@outlook.com"
EMAIL_PASSWORD = "Yrdenciri123"

msg = EmailMessage()
msg['Subject'] = 'Test #3'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Testing stuff')


def message_constructor(results_in_email):
    msg.add_alternative(results_in_email, subtype='html')
    return msg

# TODO Fix message constructor function, reddit_post email, figure out the logic and import into main module

# Configuration of the SMTP server
with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

