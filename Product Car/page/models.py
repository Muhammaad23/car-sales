from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tovar nomi", blank=True, null=True)
    description = models.TextField(verbose_name="Tovar haqida")
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Tovar narxi")
    discount_percent = models.PositiveSmallIntegerField(verbose_name="Chegirma foizi")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    county = models.CharField(max_length=100, verbose_name="County")
