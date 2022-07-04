from ast import Delete
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from apps.core_api.models import Student
from apps.core_api.api.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name', 'registration')