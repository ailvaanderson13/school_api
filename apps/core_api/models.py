from django.db import models
from . import choices


class Student(models.Model):
    registration = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(choices=choices.GENGER_CHOICES, max_length=3, default='0')
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.registration} - {self.first_name}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
