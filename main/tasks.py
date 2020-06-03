from django.core.mail import EmailMultiAlternatives
from learnDjango.celery import app
from django.core.signing import Signer
from learnDjango.settings import ALLOWED_HOSTS


@app.task
def send_notify_student(subject, html_message, from_addr, recipient_list):
    msg = EmailMultiAlternatives(subject, html_message, from_addr, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


@app.task
def send_notify_admin(subject, html_message, from_addr, recipient_list):
    msg = EmailMultiAlternatives(subject, html_message, from_addr, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


@app.task
def send_notify_teacher(subject, html_message, from_addr, recipient_list):
    msg = EmailMultiAlternatives(subject, html_message, from_addr, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

