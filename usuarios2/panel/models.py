from django.db import models

# Create your models here.
class usuarios2(models.Model):
    nombre=models.CharField(null=False, blank=False, max_length=25)
    apellido=models.CharField(null=False, blank=False, max_length=25)
    email=models.CharField(null=False, blank=False, max_length=25)

