from django.urls import path
from .import views
urlpatterns = [
    
    path('', views.obj.homepage, name="home"),
    path('product/', views.obj.product, name="product"),
    path('productdetail/<product_slug>/', views.obj.productdetail, name='productdetail'),
    path('aboutus/', views.obj.aboutus, name="about"),
   
]

