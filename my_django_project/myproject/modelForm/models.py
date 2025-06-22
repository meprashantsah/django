from django.db import models

# Create your models here.
class Project(models.Model):
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in days")

    def __str__(self):
        return self.topic

