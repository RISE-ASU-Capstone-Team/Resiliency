from django.db import models
import time


# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=100, default="")
    type = models.IntegerField(default=0)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.title
