from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact_us(request):

    # contact us functionality 

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for the message!')
            return redirect('success_contact')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact_us/contact_us.html', context)


def success_contact(request):

    return render(request, 'contact_us/success_contact.html')