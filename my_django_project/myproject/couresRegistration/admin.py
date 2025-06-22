from django.contrib import admin
from couresRegistration.models import Students,Course
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=['usn','fname','lname','email','phone','headshot']
    search_fields=['usn','fname']
    ordering=['usn']
    list_filter=['usn']
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['code','cname','createdon','view_students_link','month']
    search_fields=['code','cname']

    def month_date(self,obj):
        return obj.date.strftime("%d %B %Y")


    def view_students_link(self,obj):
        tc=obj.enrollment.count()
        url=(
            reverse('admin:capp_students_changelist')
             +"?"
             +urlencode({'course_id':f'{obj.id}'})
        )
        return format_html('<a href={}> Students{}</a>',url,tc)
    
    view_students_link.short_description="students"