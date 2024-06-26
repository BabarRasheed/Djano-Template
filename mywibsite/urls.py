"""
URL configuration for mywibsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("auth", include('auth_app.urls')),
    path("", views.index, name="home"),
    path("admin/",admin.site.urls),
    path('search/', views.search_result, name="search"),
    path('filter_products/', views.filter_products, name='filter_products'),
    path('new_arrival/', views.new_arrival_products, name='new_arrival_products'),
    path("products/<slug:category_slug>/", views.category_products_display, name="all_category_products"),
    path("brands/<slug:category_slug>/", views.category_brands_display, name="all_category_brands"),
    path("brand-products/<slug:brand_slug>/", views.brand_products_display, name="brand_products"),
    path('product_detail/<slug:product_slug>/', views.product_detail, name="product_detail"),
    path("context_us/", views.Context_us , name='context_uss'),
    path("faq/", views.FAQ_View, name='FAQ'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
