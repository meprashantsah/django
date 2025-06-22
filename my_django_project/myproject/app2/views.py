from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import timedelta

# Create your views here.

def offsetCurrentDateTime(request):
    now = datetime.datetime.now()
    aheadTime = now + timedelta(hours=4)
    behindTime = now - timedelta(hours=4)
    resp1 = "<h2>Date  and time 4 hour ahead will be : %s</h2>" %(aheadTime)
    resp2 = "<h2>Date  and time 4 hour behind will be : %s</h2>" %(behindTime)
    resp = resp1+ resp2
    return HttpResponse(resp)