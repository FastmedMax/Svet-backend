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


class Course(models.Model):
    picture = models.ImageField(verbose_name="Картинка курса", blank=True)
    title = models.CharField(verbose_name="Название курса", max_length=60)
    description = models.TextField(verbose_name="описание")
    category = models.ForeignKey(
        Category,
        verbose_name="Категория курса",
        blank=True,
        on_delete=models.CASCADE,
        related_name="courses"
        )
    lecturer = models.ForeignKey(
        Lecturer,
        verbose_name="Лектор курса",
        blank=True,
        on_delete=models.CASCADE,
        related_name="courses"
        )
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class User(AbstractUser):
    username = None
    
    first_name = models.CharField(verbose_name="Имя", max_length=60)
    last_name = models.CharField(verbose_name="Фамилия", max_length=60)
    middle_name = models.CharField(verbose_name="Отчество", max_length=60, blank=60)
    picture = models.ImageField(verbose_name="Изображение", blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
    courses = models.ManyToManyField(
        Course,
        verbose_name="Приобретённые курсы",
        blank=True,
        through="UserCourses"
        )
    email = models.EmailField(
        verbose_name="Почта",
        unique=True,
        validators=[validators.validate_email],
        error_messages={
            "unique": "Пользователь с таким email уже существует.",
        },)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    objects = UserManager()
