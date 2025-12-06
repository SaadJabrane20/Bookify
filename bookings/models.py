from django.db import models
from django.contrib.auth.models import User
from services.models import Service
# Create your models here.

class Booking(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Customer_bookings")
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provider_bookings")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return f"{self.service.name} . {self.status}"
