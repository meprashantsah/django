from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Ride(models.Model):
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    customer=models.ManyToManyField(Customer)

    def __str__(self):
        return f"{self.pickup} to {self.drop}"