from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False)

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_total_cost(self):
        total_cost = 0
        for order in self.orders.all():
            total_cost += order.product.price * order.quantity
        return total_cost
