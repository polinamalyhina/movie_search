from django.core.mail import send_mail
from core.celery import app


class Notifications:
    @staticmethod
    @app.task
    def send_email_async(subject, message, from_email, recipient_list, **kwargs):
        send_mail(subject, message, from_email, recipient_list, **kwargs)
