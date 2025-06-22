from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def show_fruits_and_students(request):
    # templates = loader.get_template("template.html")
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    students = ["Alice", "Bob", "Charlie", "David", "Eva"]

    context = {
        'fruits': fruits,
        'students': students,
    }
    return render(request,"template.html",context)
