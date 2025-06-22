from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer ,Ride
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
# Create your views here.

class CustomerListView(ListView):
    model = Customer
    context_object_name= 'customer'

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name= 'customerdetails'

def addCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("Customer added successfully")      
    else:
        form=CustomerForm()
    return render(request,"add_customer.html",{'form':form}) 


def gen_pdf(request):
    customers = Customer.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='inline;filename=customer.pdf'

    p=canvas.Canvas(response)
    p.drawString(100,700,"customer"),
    
    lh =650
    for c in customers:
        p.drawString(100,lh,f'{c.name}{c.place}{c.email}')
        lh-=20
    p.showPage()
    p.save()
    return response


def gen_csv(request):
    customers = Customer.objects.all().values()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'inline;filename=customer.csv'

    writer = csv.writer(response)
    writer.writerow(['Sl.no','name','place','email'])
    for c in customers:
        writer.writerow(c.values())
    return response
