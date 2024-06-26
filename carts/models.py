from django.db import models

from django.contrib.auth.models import User

from django.db import models
#from accounts.models import Account
from e_store.models import ProductModel

# Create your models here.
    
class CartModel(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str: 
        return self.cart_id   
    
class CartItemModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    cart=models.ForeignKey(CartModel, on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField(default=1)
    is_active=models.BooleanField(default=True)
       
    def sub_total(self):
        return self.product.discounted_price()*self.quantity
    
    def __unicode__(self) -> str:
        return self.product
     
    def __str__(self) -> str: 
        return self.product.product_name
    
class ShippingPolicy(models.Model):
    policy_point=models.CharField(max_length=50)
    
    def __str__(self) -> str: 
        return self.policy_point
    
class CheckoutInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.CharField(max_length=10)
    primary_phone = models.CharField(max_length=15)
    street_address_1 = models.TextField()
    street_address_2 = models.TextField()
    zip_code = models.CharField(max_length=10)
    
    def full_address(self):
        return f'{self.street_address_1} {self.street_address_2}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.first_name