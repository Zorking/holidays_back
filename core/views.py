import random

from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView

from core.models import Employee
from core.serializers import EmployeeSerializer


def chunk_it(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        responce = super().post(request, *args, **kwargs)
        self.send_emails()
        return responce

    def send_emails(self):
        all_males = Employee.objects.filter(is_female=False).values()
        all_females = Employee.objects.filter(is_female=True).values()
        males_chunked = chunk_it(all_males, len(all_females))
        females_chunked = chunk_it(all_females, len(all_males))[::-1]
        current_female = females_chunked[0]
        current_male_group = []
        gif_themes = ['книги', "еда"]  # TODO: add more
        for index, human in enumerate(all_males):
            if females_chunked[index]:
                if current_male_group:
                    send_mail('ID человека,которому нужно подарить подарок',
                              f'ID человека {current_female[0]["id"]}. Тема подарка {random.choice(gif_themes)}. Ваша группа {", ".join([x.get("fio") for x in current_male_group])}',
                              'zorumnipa@gmail.com',
                              [x.get('email') for x in current_male_group],
                              fail_silently=True)
                current_female = females_chunked[index]
                current_male_group = []
            else:
                current_male_group.append(human)
        send_mail('ID человека,которому нужно подарить подарок',
                  f'ID человека {current_female[0]["id"]}. Тема подарка {random.choice(gif_themes)}. Ваша группа {", ".join([x.get("fio") for x in current_male_group])}',
                  'zorumnipa@gmail.com',
                  [x.get('email') for x in current_male_group],
                  fail_silently=True)
        for index, human in enumerate(all_females):
            send_mail('ID человека,которому нужно подарить подарок',
                      f'ID людей {", ".join([str(x.get("id")) for x in males_chunked[index]])}. Тема подарка {random.choice(gif_themes)}',
                      'zorumnipa@gmail.com',
                      [human.get('email')],
                      fail_silently=True)

