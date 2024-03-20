from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=127)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.DecimalField(max_digits=10, decimal_places=2)

    objects = models.Manager()
