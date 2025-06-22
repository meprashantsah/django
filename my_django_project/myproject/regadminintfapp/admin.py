from django.contrib import admin

from regadminintfapp.models import Course, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', "student_usn", "student_sem",)
    ordering = ("student_name",)
    search_fields = ("student_name",)
    list_filter = ('student_sem',)
# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_code','course_credits')

    