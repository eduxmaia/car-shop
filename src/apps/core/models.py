from django.db import models


# Create your models here.

class Manufactor(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)


class Vehicule():
    manufactor = models.ForeignKey(Manufactor, on_delete=models.CASCADE())
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=30)
    year = models.DateTimeField()
