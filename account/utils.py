from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
import random, string
from news_exam.settings import DEFAULT_FROM_EMAIL

def generate_code():
    letters = string.ascii_letters + string.digits
    return "".join([letters[random.randint(0, len(letters)-1)] for i in range(6)])


def send_to_mail(email, code):
    subject = 'Tasdiqlash kodi'
    message = f'Kod: {code}'
    send_mail(subject=subject, message=message, from_email=DEFAULT_FROM_EMAIL, recipient_list=[email, ])
