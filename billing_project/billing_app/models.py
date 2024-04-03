from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Bill(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Bill'
