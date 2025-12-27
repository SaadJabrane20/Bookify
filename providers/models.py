from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WorkingHours(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta:
        unique_together = ("provider", "day_of_week")
    def __str__(self):
        return f"{self.provider.username}"