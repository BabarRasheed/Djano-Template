from django.contrib import admin
from .models import CategoryModel, ProductModel, ProductImagegallery, BrandModel, Productfeatures,ProductPageDescription,TagsModel,ProductReview,ExclusivePromotions,BanerAdds
import admin_thumbnails

# Register your models here.

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
    list_display = ["category", "product_name", "price","discount_percent", "stock", "is_avalible", "updated_date", "is_trending"]
    inlines = [ProductGalleryInline, ProductFeaturesInline,ProductPageDescriptionInline]

admin.site.register(ProductModel, ProductAdmin)

admin.site.register(ProductImagegallery)

admin.site.register(TagsModel)


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






















































































































































































































































































































# from django.contrib import admin
# from .models import Brand
# from .models import Brand, Category, Product, ProductImage, Discounted, FeatureDescription

# # Register your models with specific configurations.

# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('brandname', 'image')  # Corrected typo: `brandname`

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'short_description', 'brand', 'is_active')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'in_stock', 'warranty', 'price', 'is_active', 'category', 'new_arrival')  # Corrected typo: `new_arrival`

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('product', 'image') 

# @admin.register(Discounted)
# class DiscountedAdmin(admin.ModelAdmin):
#     list_display = ('discount_percentage', 'product')

# @admin.register(FeatureDescription)
# class FeatureDescriptionAdmin(admin.ModelAdmin):
#     list_display = ('product', 'detail_info','capacity','weight_dimensions', 'display', 'chip', 'iSight_camera', 'video_recording')
