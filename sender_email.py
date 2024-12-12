# mais informações: https://mailtrap.io/blog/python-send-email-gmail/
import smtplib
from email.mime.text import MIMEText

subject = "Teste de envio de E-mail"
body = "Esse é o corpo de mensagem de texto."
sender = "rogerioballoussier@gmail.com"
recipients = ["rogerioballoussier@icloud.com", "eusourogeriosb@outlook.com"]
password = "mgkh ddew apfi qvox"


def send_email(sub, bod, sen, rec, pas):
    msg = MIMEText(bod)
    msg["Subject"] = sub
    msg["From"] = sen
    msg["To"] = ", ".join(rec)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sen, pas)
        smtp_server.sendmail(sen, rec, msg.as_string())
    print("Mensagem enviada!")


send_email(subject, body, sender, recipients, password)
