from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from products.models import Product, Purchase
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Products views
class HomePage(TemplateView):
    """
    Displays Home Page (Swap home page to the blog view when it exists)
    This will be a summary of products available
    """
    template_name = 'index.html'


def home(request):
    return render(request, 'products/home.html')

# Product List View for potential customers/all users
def product_list(request):
    # Fetch all products without filtering
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


# Product Summary View for all users
# This should be for the free guides
def product_summary(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_summary.html', context)

# View to handle product purchase (for customers)
@login_required  # Ensure the user is logged in before they can purchase
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Quantity will be sent via POST form
    quantity_ordered = int(request.POST.get('quantity', 1))  # Default to one
    
    # Calculate the total price based on qty ordered
    total_price = quantity_ordered * product.price

    # Record the purchase in the Purchase model
    Purchase.objects.create(
        product=product,
        user=request.user,  # current logged in user
        quantity=quantity_ordered,
        price_paid=total_price, # Use the current product price
        status=1  # Mark as "Completed"
    )
    
    # Add success message
    messages.add_message(request, messages.SUCCESS, f"Successfully purchased {product.title}!")
    # else
    # messages.add_message(request, messages,ERROR, "Sorry, something went wrong.")
    
    # Redirect to purchase history
    return HttpResponseRedirect(reverse("purchase_history"))
    

# Purchase history
@login_required
def purchase_history(request):
    # Query for the logged-in user's purchases
    purchases = Purchase.objects.filter(
        user=request.user).order_by('-purchase_date')

    # Render the purchase history template with the purchase data
    return render(request, 'products/purchase_history.html', {'purchases': purchases})


# Fake payment view
@login_required
def fake_payment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
       
    if request.method == 'POST':
        # Simulate payment success and create a purchase
        Purchase.objects.create(
            product=product,
            user=request.user,
            quantity=1,  # Set default to 1 for simplicity
            price_paid=product.price, # Use current product price
            status=1  # Mark as "completed"
        )
        # Add success message
        messages.add_message(request, messages.SUCCESS, f'Successfully purchased {product.title}!')
    else:
        messages.add_message(request, messages,ERROR, "Sorry, purchase unsuccessful.")
   
        # Redirect to the purchase history page
        return redirect('purchase_history')
    # If not a POST request, render the fake payment page
    return render(request, 'products/fake_payment.html', {'product': product})


# Purchase success view
@login_required
def purchase_success(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/purchase_success.html', {'product': product})


# Product Detail View for logged in purchasers
# This will be the more datiled, purchased guides
@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Check if user has purchased the product
    if Purchase.objects.filter(product=product, user=request.user, status=1).exists():
        # User has purchased the product, allow access to the detailed view
        context = {
            'product': product
        }
        return render(request, 'products/product_detail.html', context)
    else:
        # User has not purchased the product, redirect or show message
        messages.error(request, "You need to purchase this product to access it.")
        return redirect('purchase_product', product_id=product.id)
