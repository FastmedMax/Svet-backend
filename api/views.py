from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Category, Course
from .serializers import CategorySerializer, CourseDetailSerializer, CuorseSerializer

# Create your views here.
