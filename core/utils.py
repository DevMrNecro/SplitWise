from django.core.mail import send_mail
from django.conf import settings
from requests import request
import schedule
import time
from django.core.management.base import BaseCommand


def send_email(request, subject, message, recipient_list,):
    subject = str(subject)
    message = str(message)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = recipient_list

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


 