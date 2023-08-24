from django import forms
from .models import Contact_Us


class ContactForm(forms.ModelForm):

    """ The Contact Us Form """

    class Meta:

        model = Contact_Us

        fields = [
            "query",
            "name",
            "email",
            "subject",
            "message",
        ]

        labels = {
            "name": "First Name",
            "query": "Reason for contacting us"
        }

        widgets = {
            "message": forms.Textarea(attrs={"rows": 9}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Enter your Name",
            "email": "Email address",
            "subject": "Subject",
            "message": "Please leave a message",
        }

        excluded_fields = ["query", "message"]

        for field_name, field in self.fields.items():
            if field_name not in excluded_fields:
                field.widget.attrs["placeholder"] = placeholders.get(field_name, "")
        self.fields["name"].widget.attrs["autofocus"] = True