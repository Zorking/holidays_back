import collections
import random

from django.core.mail import send_mail
from django.core.management import BaseCommand

from core.models import Employee
from core.utils import AnnouncementMessage, chunk_it
from holidays_back.settings import GIF_THEMES


class Command(BaseCommand):
    help = 'Creates VisitReason objects.'

    def handle(self, *args, **options):
        employees = Employee.objects.values()
        giver_que, recipient_que = employees
        random.shuffle(giver_que)
        random.shuffle(recipient_que)
        employees = collections.deque(employees)
        while employees:

            AnnouncementMessage(giver=male.get('fio'), is_female=False, recipient=current_female[0]["id"],
                                theme=random.choice(GIF_THEMES), teammates=teammates)
            send_mail('Анонс', str(message), 'zorumnipa@gmail.com', [male.get('email')], fail_silently=True)
