from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('candidate', 'Кандидат'),
        ('hr', 'HR-менеджер'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='candidate')