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
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):

    """ Adds a product to the wishlist """

    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product not in wishlist.product.all():
        wishlist.product.add(product)
        messages.info(request, f'{product.name} has been added to the wishlist')
    else:
        messages.info(request, f'{product.name} currently in the wishlist')

    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):

    """ Removes product from the wishlist """

    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.product.all():
        wishlist.product.remove(product)
        messages.info(request, f'{product.name} has been removed from the wishlist')
    else:
        messages.info(request, f'{product.name} not in your wishlist!')

    return redirect('product_detail', product_id=product_id)