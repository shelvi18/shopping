from django.db import models

class Product(models.Model):
    item=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    price=models.IntegerField()
    def __str__(self):
        return self.item
