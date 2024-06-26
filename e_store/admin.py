from django.contrib import admin
from .models import CategoryModel, ProductModel, ProductImagegallery, BrandModel, Productfeatures,ProductPageDescription,TagsModel,ProductReview,ExclusivePromotions,BanerAdds, ProductVariation
import admin_thumbnails

# Register your models here.
class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]

admin.site.register(CategoryModel, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]

admin.site.register(BrandModel, BrandAdmin)

@admin_thumbnails.thumbnail("image")
class ProductGalleryInline(admin.TabularInline):
    model = ProductImagegallery
    extra = 1
    
class ProductFeaturesInline(admin.TabularInline):
    model = Productfeatures
    extra = 1
    
class ProductPageDescriptionInline(admin.TabularInline):
    model = ProductPageDescription
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
    list_display = ["category", "product_name", "price", "discount_percent", "stock", "is_avalible", "updated_date", "is_trending"]
    search_fields = ('product_name',)  # Enable search by product_name
    inlines = [ProductGalleryInline, ProductFeaturesInline, ProductPageDescriptionInline, ProductVariationInline]

admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProductImagegallery)
admin.site.register(TagsModel)
admin.site.register(ProductVariation)
admin.site.register(ProductReview)
admin.site.register(ExclusivePromotions)
admin.site.register(BanerAdds)

























# from django.contrib import admin
# from .models import CategoryModel,ProductModel,ProductImagegallery,BrandModel
# import admin_thumbnails
# # Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={"slug":("category_name",)}
#     list_display=["category_name","slug"]
    
    
# admin.site.register(CategoryModel,CategoryAdmin)  


# class BrandAdmin(admin.ModelAdmin):
#     prepopulated_fields={"slug":("brand_name",)}
#     list_display=["brand_name","slug"]
    
    
# admin.site.register(BrandModel,CategoryAdmin)  


    
# @admin_thumbnails.thumbnail("image")
# class ProductGalleryInline(admin.TabularInline):
#     model=ProductImagegallery
#     extra=1

# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields={"slug":("product_name",)}
#     list_display=["category","product_name","price","stock","is_avalible","updated_date"]
#     inlines=[ProductGalleryInline]
    

# admin.site.register(ProductModel,ProductAdmin)


# admin.site.register(ProductImagegallery)
