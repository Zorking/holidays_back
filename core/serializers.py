from django.core.mail import send_mail
from rest_framework.serializers import ModelSerializer

from core.models import Employee
from core.utils import RegistrationMessage


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        message = RegistrationMessage(instance.fio)
        send_mail('Регистрация', str(message), 'zorumnipa@gmail.com', [instance.email], fail_silently=False)
        return instance
