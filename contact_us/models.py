from django.db import models

# Create your models here.


class Contact_Us(models.Model):

    query_reason = [
        ('Stock', 'Stock'),
        ('Delivery', 'Delivery'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    query = models.CharField(max_length=50, choices=query_reason, default='Other', null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=30)
    email = models.EmailField(null=False, blank=False, max_length=50)
    on_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(null=False, blank=False, max_length=20)
    message = models.TextField()
    

    def __str__(self):
        
        return f"{self.name} contacted us"