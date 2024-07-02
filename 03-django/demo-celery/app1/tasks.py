import time
from celery import shared_task


@shared_task
def send_mail(to):
    #time.sleep(2)
    print(f"Email enviado a {to}.")


@shared_task
def send_welcome_mail(to):
    print(f"Welcome Email enviado a {to}.")
    return to


@shared_task
def send_tip_mail(to):
    print(f"Tip Email enviado a {to}.")
    return to


@shared_task
def send_newsletter_mail(to):
    print(f"Newsletter Email enviado a {to}.")
    return to


@shared_task
def update_mails_sent(*args):
    print("Todos los correos fueron enviados.")