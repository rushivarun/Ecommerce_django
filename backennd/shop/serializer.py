from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Product
        fields = ('category', 'name', 'price', 'id')


class DetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Product
        fields = ('category', 'name', 'price', 'description', 'available', 'created')



