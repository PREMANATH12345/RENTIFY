from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    nearby_facilities = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class InterestedBuyer(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer.username} interested in {self.property.title}'
