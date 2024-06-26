from django.urls import path
from carts import views
urlpatterns = [
    path('', views.view_cart, name='viewcart'), 
    # path('checkout/', views.check_out, name='checkcart'), 
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout_info/', views.checkout_info, name='checkout_info'),
    path('check_out/', views.check_out, name='check_out'),
    path('saveinfo/', views.save_info, name='save_info'),
    path("remove/<int:product_id>", views.remove_from_cart, name="remove_cart"),
    path("payment/", views.payment, name="payment"),
    path('cartcomplete/', views.cart_complete, name='cart_complete'),
    path('Payment_cart/', views.Payment_cart.as_view(), name='Payment_cart'),

]