import uuid

from django.core.management import BaseCommand

from core.models import Employee


class Command(BaseCommand):
    help = 'Creates VisitReason objects.'

    def handle(self, *args, **options):
        for i in range(25):
            id = uuid.uuid4().hex
            Employee.objects.create(fio=id, email=f"{id}@gmail.com", is_female=True if i % 4 == 0 else False)
