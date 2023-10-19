from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """A model for a user's wishlist"""

    product = models.ManyToManyField(Product, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
            return self.product.name