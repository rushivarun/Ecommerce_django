from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductViews.as_view(), name='products'),
]
