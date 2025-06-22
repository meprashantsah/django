from django.shortcuts import render
from .models import Student,Course
from django.views.generic import ListView,DetailView
# Create your views here.

class StudentListView(ListView):
    model = Student
    context_object_name ='student_list' #context_object_name should be same

class StudentDetailView(DetailView):
    model = Student