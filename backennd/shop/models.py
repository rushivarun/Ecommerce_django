from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta():
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    
    def get_price(self):
        return self.sale_price if self.sale_price else self.price

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return self.category

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     sale_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return self.product.name

#     def get_price(self):
#         return self.sale_price if self.sale_price else self.price

#     def add_to_cart(self):
        


