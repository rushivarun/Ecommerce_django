from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Product
        fields = ('category', 'name', 'description',
                  'price', 'stock', 'available', 'updated')
