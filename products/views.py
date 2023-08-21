from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.
def all_products(request):
    """ A view for displaying all aproducts and sorting and searching queries"""

    products = Product.objects.all()
    query = None

    """
    Verify the presence of the Category; if found, divide it into a list using commas,
    which will then be employed to narrow down the queryset of all products to those that correspond.
    """
    if 'q' in request.GET:
        query = request.GET['q']

        if not query:
            messages.error(
                request, 'You did not enter any search criteria')
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

        products = products.filter(queries)    

    context = {
        'products': products,
         'search_term': query,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show details of product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)