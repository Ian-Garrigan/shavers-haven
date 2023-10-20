from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile


# Create your views here.
def all_products(request):
    """ A view for displaying all aproducts and sorting and searching queries"""

    products = Product.objects.all()
    query = None
    categories = None 
    sort = None
    direction = None

    # Check if sort fileter is requested by user
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    """
    Verify the presence of the Category; if found, divide it into a list using commas,
    which will then be employed to narrow down the queryset of all products to those that correspond.
    """

    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']

        if not query:
            messages.error(
                request, 'You did not enter any search criteria')
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting' : current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show details of product"""

    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product).order_by("-created_on")


    context = {
        'product': product,
        'review' : review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

        template = 'products/add_product.html'
        context = {
            'form': form,
        }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def add_review(request, product_id):
    """publish a review from user"""

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            try:
                Review.objects.create(
                    product=product,
                    user=request.user,
                    name=request.POST["name"],
                    review=request.POST["review"],
                )
                reviews = Review.objects.filter(product=product)
                messages.info(request, "You added a review")
                return redirect(reverse("product_detail", args=[product.id]))
            except IntegrityError:
                messages.error(request, "You have reviewed this product already.")
                return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Submission failed, please try again.")
    return redirect(reverse("product_detail", args=[product.id]))
