from django.shortcuts import render

from e_store.models import ProductModel, ProductImagegallery, Productfeatures, ProductPageDescription, ProductReview, ProductVariation


# Create your views here.

class Epage():

    def homepage(self, request):
        return render(request, 'index.html')
    def product(self, request):
        return render(request, 'product.html')

    def productdetail(self, request, product_slug): 
        product=ProductModel.objects.get(slug= product_slug)
        product_images=ProductImagegallery.objects.filter(product=product)
        product_features=Productfeatures.objects.filter(product=product)
        product_description=ProductPageDescription.objects.filter(product=product)
        variations = ProductVariation.objects.filter(product=product).order_by('main_title', 'title')
        ProductReview.objects.filter(product=product)

        reviews=ProductReview.objects.filter(status=True, product=product)
        context={ 
        "product":product,
        "product_images":product_images,
        "product_features":product_features,
        "product_description":product_description,
        "reviews":reviews, 
        "variations" : variations
        }
    
        return render (request, "product_detail.html",context)
    
    def aboutus(self, request):
        return render(request, 'about_us.html')
    
obj = Epage()