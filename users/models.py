from django.db import models
from django.contrib.auth.models import User
from services.models import ServiceCategory
# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = (
        ('provider', 'Provider'),
        ('client', 'Client'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='client'
    )
    phone_number = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(
        ServiceCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.user.username} Profile"
