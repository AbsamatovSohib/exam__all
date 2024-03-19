from rest_framework import serializers
from task3.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "price", "marja", "package_code")
