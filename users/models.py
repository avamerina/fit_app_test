from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BaseProfile(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('trainer', 'Trainer')
    ]
    GENDER_CHOICES = [
        ('female', 'Female'),
        ("male", "Male"),
        ("not_specified", "Not specified")
    ]
    role = models.CharField(max_length=100, choices=ROLES, default='client')
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=30,
        choices=GENDER_CHOICES,
        default="not_specified"
    )
    is_active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['role', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.role} {self.username}"

    class Meta:
        verbose_name = "base_profile"
        verbose_name_plural = "base_profiles"
        db_table = 'base_profiles'
