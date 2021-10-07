from internet_speed.settings.base import user_mail
from internet_speed.cron.generate_reports import generate_report
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os

path = "internet_speed/local_data"

def send_email():
    print("Sending email...")
    ctx = generate_report()

    message_txt = render_to_string("email_template.txt", ctx)
    message_html = render_to_string("email_template.html", ctx)

    mail = EmailMultiAlternatives("Internet Speed Report", message_txt, to=[user_mail,])
    for image in os.listdir(path):
        mail.attach_file(path+"/"+image)
    mail.attach_alternative(message_html, "text/html")
    mail.send()


