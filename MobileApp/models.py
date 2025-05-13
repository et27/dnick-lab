from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):

    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date_of_creation=models.DateField()
    is_in_eu=models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.location}"


class MobilePhone(models.Model):
    TYPE_CHOICES = [
       ("S", "Small"),
       ("M", "Medium"),
       ("L", "Large"),
    ]

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to="mobile_photos/", null=True, blank=True)
    price=models.IntegerField()
    year_of_production=models.DateField(null=True, blank=True)
    new_user=models.BooleanField()



    def __str__(self):
        return f"{self.model} {self.manufacturer}"
