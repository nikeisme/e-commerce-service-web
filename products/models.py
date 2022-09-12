from django.db import models

from commons.models import TimeStampedModel


class Category(models.Model):

    name = models.CharField(max_length=45)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Product(TimeStampedModel):

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = "products"

        def __str__(self):
            return self.name


class ProductImage(TimeStampedModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name="image")
    image = models.ImageField(upload_to='profile/',default='default.png')

    class Meta:
        db_table = "products_images"

    def __str__(self):
        return self.name
