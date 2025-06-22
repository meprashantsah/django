from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def CurrentDateTime(request):
    now = datetime.datetime.now()
    resp = "<h2>Current Date and time : %s</h2>" %(now)
    return HttpResponse(resp)
