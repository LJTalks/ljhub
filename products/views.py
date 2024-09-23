from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Product, Purchase
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Products views

class HomePage(TemplateView):
    """
    Displays Home Page (Swap home page to the blog view when it exists)
    This will be a summary of products available
    """
    template_name = 'index.html'


def home(request):
    return render(request, 'products/home.html')

# Product List View for potential customers
def product_list(request):
    products = Product.objects.filter(status=1) # did we give our products a status?)
    
    
# Product Details View for potential customers
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)

# View to handle product purchase (for customers?)
@login_required  # Ensure the user is logged in before they can purchase
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Quantity will be sent via POST form
    quantity_ordered = int(request.POST.get('quantity', 1))  # Default to one

    # Check if stock is available/
    if product.stock >= quantity_ordered:
        # Decrease stock by number bought/ordered (Before checking for alerts or pricing)
        product.stock -= quantity_ordered
        product.save()

        # Check for low stock and send an email if below threshold
        if product.stock <= product.low_stock_threshold and not product.low_stock_alert_sent:
            send_mail(
                'Low Stock Alert',
                f'The Product {product.title} is running low on stock.',
                'admin@test.com',
                ['admin@test.com']
            )
            product.low_stock_alert_sent = True  # Mark that alert has been sent
            product.save()

        # Tiered pricing (e.g. first 100 are free, remaining at £4.99)
        if product.stock >= product.tier_one_limit:
            total_price = 0  # Tier One price (free)
        else:
            remaining_at_tier_one = max(
                product.tier_one_limit - product.stock, 0)
            price_tier_one = remaining_at_tier_one * product.tier_one_price
            price_tier_two = (quantity_ordered -
                              remaining_at_tier_one) * product.price
            total_price = price_tier_one + price_tier_two

        # Check if product is limited to one per customer
        if product.limit_one_per_customer and quantity_ordered > 1:
            return HttpResponse("This product is limited to one per customer.")

        # Record the purchase in the Purchase model
        Purchase.objects.create(
            product=product,
            user=request.user,  # current logged in user
            quantity=quantity_ordered,
            price_paid=total_price,
            status=1  # Mark as "Completed"
        )

        return HttpResponse(f"Successfully purchased {product.title}!")
    else:
        return HttpResponse("Sorry, there is not enough stock available.")


@login_required
def purchase_history(request):
    # Query for the logged-in user's purchases
    purchases = Purchase.objects.filter(
        user=request.user).order_by('-purchase-date')

    # Render the purchase history template with the purchase data
    return render(request, 'purchase_history.html', {'purchases': purchases})
