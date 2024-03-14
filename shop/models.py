from django.db import models
from utils.models import BaseModel
from users.models import User
# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=31)


class Product(BaseModel):
    title = models.CharField(max_length=31)
    description = models.TextField()
    image = models.ImageField(upload_to='images/shop/')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2, help_text='Enter the price in decimal format (exp: 10.99)')
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE, related_name='products')


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    class Meta:
        unique_together = ('product', 'rating')





class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_address')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_address')
    fullname = models.CharField(max_length=31)
    address = models.CharField(max_length=31)

    landmark = models.CharField(max_length=31)
    city = models.CharField(max_length=31)

    pincode = models.CharField(max_length=31)
    contact_number = models.CharField(max_length=7)







