from django.contrib import admin
from .models import Student
from .models import Project
# Register your models here.

admin.site.register(Student)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["Selected_student", "Topic", "Languages_used", 'Duration_in_days']

