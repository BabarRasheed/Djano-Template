from .models import CategoryModel,BrandModel,ProductModel

def all_categories_tem(request):
    all_categories=CategoryModel.objects.all()
    return {'all_categories':all_categories}
    # return dict(all_categories=all_categories)

def all_brands_tem(request):
    all_brands=BrandModel.objects.all()
    return {'all_brands':all_brands}
    # return dict(all_brands=all_brands)

def latest_items_tem(request):
    latest_items=ProductModel.objects.all().order_by('-created_date')[:4]
    return dict(latest_items=latest_items)