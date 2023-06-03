from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Types(models.TextChoices):
        STUDENT = "Student"
        MANAGER = "Manager"
        TEACHER = "Teacher"
        
    type = models.CharField(max_length=50, choices=Types.choices)
    phone_number = models.CharField(max_length=11, null=True)
    national_id = models.CharField(max_length=10, null=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name