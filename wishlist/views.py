from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponseRedirect,
    get_object_or_404,
)
from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """
    Render wishlist for logged in user
    """
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


