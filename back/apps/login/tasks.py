from django.core.mail import send_mail

from config.settings import EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL, SERVER_EMAIL

from celery import shared_task

from .utils import generate_jwt_token


@shared_task()
def send_confirmation_email_task(username, email):
        token = generate_jwt_token()
        send_mail(
                subject='Confirmation',
                message=f'Dear {username}, Thank you for using our service\
                        Check the link below to registrate http://127.0.0.1:8000/registration?token={token} ',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
                auth_user=DEFAULT_FROM_EMAIL,
                auth_password=EMAIL_HOST_PASSWORD
                )



