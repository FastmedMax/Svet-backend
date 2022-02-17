from django.contrib import admin

from .models import Category, Course, Lecturer, User, UserCourses

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lecturer)


class CourseList(admin.StackedInline):
    model = User.courses.through
    extra = 0
    classes = ["collapse"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (CourseList,)
    exclude = (
        "password", "groups", "is_active",
        "is_staff", "is_superuser", "last_login",
        "date_joined", "user_permissions"
        )