import random

from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView

from core.models import Employee
from core.serializers import EmployeeSerializer


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer
