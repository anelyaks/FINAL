from django.contrib import admin
from .models import Category, Product, buy


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['category','level', 'type', 'price', 'slug','available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('type',)}

@admin.register(buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
