from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Category, Course
from .serializers import CategorySerializer, CourseDetailSerializer, CuorseSerializer

# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category
    serializer_class = CategorySerializer

    def get(self, request):
        try:
            categories = self.queryset.objects.all()
        except Category.DoesNotExist:
            return Response("Категории не найдены!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDetailView(APIView):
    """Find selected course for id and full info"""
    queryset = Course
    srializer_class = CourseDetailSerializer

    def get(self, request, id):
        try:
            course = self.queryset.objects.get(id=id)
        except Course.DoesNotExist:
            return Response("Курс не найден!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.srializer_class(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
