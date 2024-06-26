from django.shortcuts import render
from django.shortcuts import redirect
from .models import ProductModel,BrandModel,CategoryModel,ProductImagegallery,Productfeatures,ProductPageDescription,TagsModel,ProductReview,ExclusivePromotions,BanerAdds
from django.core.paginator import Paginator
from datetime import date
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BanerAdds, CategoryModel, ProductModel
from datetime import date

def index(request):
    current_date = date.today()
    adds = BanerAdds.objects.all()
    categories = CategoryModel.objects.prefetch_related('brandmodel_set', 'productmodel_set').all()
    trending_items = ProductModel.objects.filter(is_trending=True)[:6]
    context = {
        'trending_items':trending_items ,
        "categories": categories,
        'adds': adds, 
    }
    return render(request, 'index.html', context)

def  product_detail(request, product_slug):
    product=ProductModel.objects.get(slug=product_slug)
    context={
        'product':product,
    }
    return render (request, "product_detail.html",context)

def category_products_display(request,category_slug ):
    category=CategoryModel.objects.get(slug=category_slug)
    products=ProductModel.objects.filter(category=category)
    items_per_page = 9
    paginator = Paginator(products, items_per_page)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)
    context={
        "category":category,
        "products":items_page,
        "products_count":len(products),
    }
    return render (request, "product.html", context)

def brand_products_display(request,brand_slug):
    brand=BrandModel.objects.get(slug=brand_slug)
    products=ProductModel.objects.filter(brand=brand)
    items_per_page = 4
    paginator = Paginator(products, items_per_page)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)
    context={
        "category":brand,
        "products":items_page,
        "products_count":len(products),
    }
    return render (request, "product.html", context)

def category_brands_display(request, category_slug):
    category = CategoryModel.objects.get(slug=category_slug)
    sort_parameter = request.GET.get('sort')
    sort_key = 'name'  

    if sort_parameter == 'popular':
        sort_key = '-is_popular'  

    brands = BrandModel.objects.filter(category=category).order_by(sort_key)
    items_per_page = 9
    paginator = Paginator(brands, items_per_page)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)
    context = {
        "category": category,
        "brands": items_page,
        "brands_count": len(brands),
    }
    return render(request, "brands.html", context)
def new_arrival_products(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    new_arrival_products = ProductModel.objects.filter(created_date__gte=one_month_ago)
    items_per_page = 2
    paginator = Paginator(new_arrival_products, items_per_page)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)
    context = {
        'products': items_page,
        'products_count': len(new_arrival_products),
    }
    return render(request, 'product.html', context)
def search_result(request):
    context = {}

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = ProductModel.objects.filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword) |
                Q(tags__tag__icontains=keyword)
            ).distinct()
            items_per_page = 9  
            paginator = Paginator(products, items_per_page)
            page_number = request.GET.get('page')
            items_page = paginator.get_page(page_number)
            context['products'] = items_page
            context['products_count'] = len(products)

    return render(request, "product.html", context)

def filter_products(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        products = ProductModel.objects.filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword) |
                Q(tags__tag__icontains=keyword)
            ).distinct()

        context = {
            'products': products,
            'products_count':len(products),
            "keyword":keyword,
        }
        return render(request, 'brands.html', context)
    else:
        return render(request, 'product.html')
def Context_us(request):
    return render(request, 'contact_us.html')

def FAQ_View(request):
    return render(request,'faq.html')