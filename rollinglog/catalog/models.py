from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class RollingPaper(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    flavor = models.CharField(max_length=100, blank= True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    #Relatioships 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
