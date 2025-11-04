from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('paper-detail', kwargs={'pk': self.id})
    
    
    
class Review(models.Model):
    paper = models.ForeignKey(RollingPaper, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.paper.name}"



    
    

    def __str__(self):
        return self.name
    

