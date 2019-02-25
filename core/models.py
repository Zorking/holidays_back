import uuid

from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    is_female = models.BooleanField()
