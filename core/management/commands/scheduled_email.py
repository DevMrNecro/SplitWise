# your_app/management/commands/send_scheduled_email.py
import schedule
import time
from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
from .utils import send_email
from requests import request

#this yet not working async for now
#to run this: python3 manage.py scheduled_email

class Command(BaseCommand):
    help = 'Send scheduled email weekly'

    def handle(self, *args, **options):
        # Schedule the task to run every Monday at midnight
        schedule.every().wednesday.at("15:39").do(self.send_email)

        # Run the scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_email(self):
        subject = 'Weekly update'
        message = 'message'
        lst = ['ojasbarik@gmail.com', 'ojasbarik2211@gmail.com']
        send_email(request, subject, message, lst)

        self.stdout.write(self.style.SUCCESS('Successfully sent scheduled emails.'))
    