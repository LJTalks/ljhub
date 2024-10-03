from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Product models

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True) # Short summary for public view
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=100)
    related_products = models.ManyToManyField('self', blank=True) # New field to link related products

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if slug is not set
            self.slug = slugify(self.title)  # Generate slug from name
        # If the stock is replenished, reset low_stock_alert_sent to false
        # if self.stock > self.low_stock_threshold:
            # self.low_stock_alert_sent = False
        super().save(*args, **kwargs)  # Call the parent class save method

    def __str__(self):
        return self.title  # Use title for string representation


# Purchases model


class Purchase(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Completed'),
        (2, 'Refunded'),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)
    # capturing price_paid is important as product price may subsequently change,
    # user may have recived an offer or discount
    price_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.product.title} ({self.get_status_display()})"
