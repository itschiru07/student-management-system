from django.contrib import admin
from .models import Department, course, Student


@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'code', 'credits')
    


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'building')
   


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'cgpa')
    list_filter = ('department', 'gender')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__username')
    filter_horizontal = ('courses',)
