from django.contrib import admin

from django.contrib import admin
from .models import CartItemModel,CartModel,ShippingPolicy,CheckoutInformation
import admin_thumbnails

# Register your models here.


admin.site.register(CartItemModel)

admin.site.register(CartModel)
admin.site.register(ShippingPolicy)
admin.site.register(CheckoutInformation)

