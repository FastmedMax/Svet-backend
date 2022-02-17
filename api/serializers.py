from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

from .models import Category, Course, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
