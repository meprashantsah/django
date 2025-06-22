from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm


# Create your views here.

def addProject(request):
    if(request.method=='POST'):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Added Successfully")
    else:
        form=ProjectForm()
    return render(request,'add_project.html',{'form':form})