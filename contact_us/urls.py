from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('success_contact/', views.success_contact, name='success_contact'),
]