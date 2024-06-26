from .models import CartItemModel,CartModel
from .views import cart_id

def cart(request):
    cart_items = None
    try:
        cart=CartModel.objects.get(cart_id=cart_id(request))
        cart_items=CartItemModel.objects.filter(cart=cart, is_active=True)
    except:
        pass
        
    return dict(cart_items=cart_items)

def counter(request):
    cart_count = 0
    some_other_variable = 'Some value'

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = CartModel.objects.filter(cart_id=cart_id(request))
            cart_items = CartItemModel.objects.filter(cart=cart[:1])
            cart_count=len(cart_items)
        except CartModel.DoesNotExist:
            cart_count = 0
            
            
    return {
        'cart_count': cart_count,
        'some_other_variable': some_other_variable,
        # Add more variables as needed
    }