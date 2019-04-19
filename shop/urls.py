from django.urls import path, re_path
from . import views


urlpatterns = [
    path('products/', views.ProductViews.as_view(), name='products'),
    re_path('(?P<pk>\d+)/', views.DetailViews.as_view(), name='details'),
]
