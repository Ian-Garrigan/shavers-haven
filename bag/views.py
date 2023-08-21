from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A view to return the shopping bag contents page"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Place the specified quantity of the product into the shopping bag. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    
# Adjust amount of product in the shopping bag
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))

    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f"Updated {product.name} quantity to {bag[item_id]}")
    else:
# Delete by pop func
        bag.pop(item_id)
        messages.success(
            request, f"Removed {product.name} from your bag")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))    