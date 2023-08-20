from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """
    Display the Category model fields in the admin view
    """

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Display the Product model fields in the admin view
    """

    list_display = (
        'friendly_name',
        'name',
    )
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
