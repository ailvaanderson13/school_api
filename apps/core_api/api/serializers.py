from rest_framework.serializers import ModelSerializer
from apps.core_api.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
