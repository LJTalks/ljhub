from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Product

# Products views


class HomePage(TemplateView):
    """
    Displays Home Page
    """
    template_name = 'index.html'


# View to handle product purchase
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if stock is available
    if product.stock > 0:
        # Decrease stock by number bought/ordered
        product.stock -= 1
        product.save()

        # Purchase handling logic
        return HttpResponse(f"Successfully purchased {product.title}!")
    else:
        return HttpResponse("Sorry, this product is out of stock.")
