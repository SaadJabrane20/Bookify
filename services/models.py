from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name