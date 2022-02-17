from django.db import models

from django.core import validators
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=60)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

