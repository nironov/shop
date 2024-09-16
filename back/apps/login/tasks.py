from django.core.mail import send_mail

from config.settings import EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL, SERVER_EMAIL

from celery import shared_task
import jwt


@shared_task()
def send_confirmation_email_task(username, email):
        send_mail(
                subject='Confirmation',
                message=f'Dear {username}, Thank you for using our service',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
                auth_user=DEFAULT_FROM_EMAIL,
                auth_password=EMAIL_HOST_PASSWORD
                )


encoded_jwt = jwt.encode({'some':'my paylopoad'}, 'secret')
# Сделать функционал проверки юзера по JWT токену

