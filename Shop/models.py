from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    msg = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name