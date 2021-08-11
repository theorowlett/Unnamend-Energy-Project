from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.models import USStateField

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Data(models.Model):
    state = USStateField(null=True, blank=True)
    slope = models.FloatField(null=True)
    intercept = models.FloatField(null=True)

    def __str__(self) -> str:
        return self.state

class Annual_Data(models.Model):
    state = models.ForeignKey(Data, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    def __str__(self) -> str:
        return str(self.year)