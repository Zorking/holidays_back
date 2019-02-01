import random

from django.core.mail import send_mail
from django.core.management import BaseCommand

from core.models import Employee
from core.views import chunk_it


class Command(BaseCommand):
    help = 'Creates VisitReason objects.'

    def handle(self, *args, **options):
        send_mail('ID человека,которому нужно подарить подарок',
                  "qwe",
                  'zorumnipa@gmail.com',
                  ["zorumnipa@gmail.com"],
                  fail_silently=False)
