from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product (models.Model):
    title = models.CharField (max_length=50)
    price = models.IntegerField(blank=True)
    exist = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='productImages/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + self.user.username
     