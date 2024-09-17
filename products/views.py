from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Product

# Products views


class HomePage(TemplateView):
    """
    Displays Home Page (Swap home page to the blog view when it exists)
    This will be a summary of products available
    """
    template_name = 'index.html'


# View to handle product purchase
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if product is limited to one per customer
    if product.limit_one_per_customer and quantity_ordered > 1:
        return HttpResponse("This product is limited to one per customer.")

    # Quantity will be sent via POST form
    quantity_ordered = int(request.POST.get('quantity', 1))  # Default to one

    # Check if stock is available
    if product.stock >= quantity_ordered:
        # Decrease stock by number bought/ordered
        product.stock -= quantity_ordered
        product.save()

        # Tiered pricing (e.g. first 100 are free, remaining are £4.99)
        if product.stock >= 100:
            total_price = 0  # Free for the first 100
        else:
            total_price = (100 - product.stock) * \
                4.99  # £4.99 for items beyond 100

        # Purchase handling logic
        return HttpResponse(f"Successfully purchased {product.title}!")
    else:
        return HttpResponse("Sorry, there is not enough stock available.")
