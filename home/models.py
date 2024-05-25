from django.db import models

# Create your models here.

class Car (models.Model):
    name = models.CharField (max_length=50)
    desc = models.CharField (max_length=120)
    active = models.BooleanField (default=False)

    def __str__(self):
        return self.name
    