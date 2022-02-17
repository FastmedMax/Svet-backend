from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

from .models import Category, Course, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CreateUserSerializer(DjoserUserCreateSerializer):

    class Meta:
        model = User
        exclude = ("last_login", "date_joined",
                   "is_superuser", "is_staff", "is_active", 
                   "groups", "user_permissions")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CuorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "picture", "title")
