from django.urls import path

from .views import CategoryListView, CourseDetailView, CourseListView
urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("courses/", CourseListView.as_view()),
    path("courses/<str:id>/", CourseDetailView.as_view()),
]
