from django.db import models

from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.
class Category(models.Model):
    """
    Model for assigning shaving shop categories
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """
        Fix for django admin naming convention
        """
        verbose_name_plural = "Categories"

    def __str__(self):
        """Returns Category model name"""
        return self.name

    def get_friendly_name(self):
        """
        Passes friendly name to admin
        """
        return self.friendly_name    


class Product(models.Model):
    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Returns Category model name"""
        return self.name


class Review(models.Model):
    """
    Model for reviewing a product
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    review = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name