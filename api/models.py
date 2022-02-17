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


class Lecturer(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=60)
    last_name = models.CharField(verbose_name="Фамилия", max_length=60)
    middle_name = models.CharField(verbose_name="Отчество", max_length=60, blank=60)
    photo = models.ImageField(verbose_name="Фотография", blank=True)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Лектор"
        verbose_name_plural = "Лекторы"
