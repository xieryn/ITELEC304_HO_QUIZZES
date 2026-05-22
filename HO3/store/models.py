from django.db import models


class Product(models.Model):
    item_name = models.CharField(max_length=120)
    item_price = models.FloatField()

    def product_info(self):
        return f"{self.item_name} is worth ₱{self.item_price}"

    def __str__(self):
        return self.item_name
