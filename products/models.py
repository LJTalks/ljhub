from django.db import models
from django.contrib.auth.models import User

# Product models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    limit_one_per_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Commented out purchases fo testing as it's not yet defined
# class Purchases(models.Model):
#     STATUS_CHOICES = [
#         (0, 'Pending'),
#         (1, 'Completed'),
#         (2, 'Refunded'),
#     ]
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="purchases")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     purchase_date = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS_CHOICES, default=0)

#     def __str__(self):
#         return f"{self.user.username} - {self.product.title} ({self.get_status_display()})"
