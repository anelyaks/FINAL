from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('abonements:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    level = models.CharField('level', max_length=50, db_index=True)
    type = models.CharField('type', max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('type',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('abonements:product_detail', args=[self.id, self.slug])

class buy(models.Model):
    name = models.CharField('name', max_length=50, db_index=True)
    number = models.CharField('number', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'buyer'
        verbose_name_plural = 'buyers'