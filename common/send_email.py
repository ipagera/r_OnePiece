
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "yvann.jeronimo12@gmail.com"
EMAIL_PASSWORD = "Yrdenciri123"

msg = EmailMessage()
msg['Subject'] = 'Test #3'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Testing stuff')

msg.add_alternative("""\ 
    
    """, subtype='html')

# Configuration of the SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()