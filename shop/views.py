from django.shortcuts import render
from . import serializer
from rest_framework import generics
from . import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.


class ProductViews(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('category', 'price', 'available',)
    ordering_fields = ('price', 'stock')
    search_fields = ('name',)
