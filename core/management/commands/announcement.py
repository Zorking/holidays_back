import random

from django.core.mail import send_mail
from django.core.management import BaseCommand

from core.models import Employee
from core.utils import AnnouncementMessage, chunk_it
from holidays_back.settings import GIF_THEMES


class Command(BaseCommand):
    help = 'Creates VisitReason objects.'

    def handle(self, *args, **options):
        all_males = Employee.objects.filter(is_female=False).values()
        all_females = Employee.objects.filter(is_female=True).values()
        males_chunked = chunk_it(all_males, len(all_females))
        females_chunked = chunk_it(all_females, len(all_males))[::-1]
        current_female = females_chunked[0]
        current_male_group = []

        for index, human in enumerate(all_males):
            if females_chunked[index]:
                if current_male_group:
                    self.send_messages_male(current_female, current_male_group)
                current_female = females_chunked[index]
                current_male_group = []
            else:
                current_male_group.append(human)
        self.send_messages_male(current_female, current_male_group)
        for index, human in enumerate(all_females):
            recipient = ", ".join([str(x.get("id")) for x in males_chunked[index]])
            message = AnnouncementMessage(giver=human.get('fio'), is_female=True, recipient=recipient,
                                          theme=random.choice(GIF_THEMES), teammates=None)
            send_mail('Анонс', str(message), 'zorumnipa@gmail.com', [human.get('email')], fail_silently=True)

    def send_messages_male(self, current_female, current_male_group):
        teammates = ", ".join([x.get("fio") for x in current_male_group])
        for male in current_male_group:
            message = AnnouncementMessage(giver=male.get('fio'), is_female=False, recipient=current_female[0]["id"],
                                          theme=random.choice(GIF_THEMES), teammates=teammates)
            send_mail('Анонс', str(message), 'zorumnipa@gmail.com', [male.get('email')], fail_silently=True)
