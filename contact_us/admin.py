from django.contrib import admin
from .models import Contact_Us
# Register your models here.

class Contact_Us_Admin(admin.ModelAdmin):

    list_display = (
        "query_reason",
        "name",
        "email",
        "on_date",
        "subject",
        "message",
    )

    list_filter = ("on_date", "name")

    ordering = ("-on_date",)

admin.site.register(Contact_Us, Contact_Us_Admin)    