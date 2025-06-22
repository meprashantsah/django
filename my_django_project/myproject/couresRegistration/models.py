from django.db import models
from datetime import date


# Create your models here.
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    usn=models.CharField(max_length=10,unique=True)
    fname=models.CharField(max_length=80)
    lname=models.CharField(max_length=80)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    headshot=models.ImageField(upload_to='temp/')
    

    def __str__(self):
        return f'{self.usn} {self.fname} {self.lname}'
    

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.CharField(max_length=10,unique=True)
    cname=models.CharField(max_length=80)
    c_credits=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    enrollment=models.ManyToManyField(Students)
    createdon=models.DateField(default=date.today(),null=True)
    month=models.DateField(default=date.today(),null=True)
    

    def __str__(self):
        return f'{self.code} {self.cname}'