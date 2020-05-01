from django.db import models


# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
