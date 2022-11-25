from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    price = models.IntegerField()
