from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.db.models import Avg,Count
# from accounts.models import Account
# Create your models here
from django.core.exceptions import ValidationError
from django.utils import timezone

class CategoryModel(models.Model):
    name                =models.CharField(unique=True ,max_length=50)
    description         =models.TextField(blank=True, max_length=255)
    cate_image          =models.ImageField(upload_to="uploads/category", blank=True)
    slug                =models.SlugField(unique=True, max_length=100)
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        
    def related_brands(self):
        return BrandModel.objects.filter(category=self)
    
    def related_products(self):
        return ProductModel.objects.filter(category=self, is_avalible=True, discount_percent__gt=2)
        
    def __str__(self) -> str:
        return self.name

class BrandModel(models.Model):
    is_popular          =models.BooleanField(default=False)
    category            =models.ManyToManyField(CategoryModel)
    name                =models.CharField(unique=True ,max_length=50)
    description         =models.TextField(blank=True, max_length=255)
    brand_image         =models.ImageField(upload_to="uploads/brand", blank=True)
    slug                =models.SlugField(unique=True, max_length=100)
    
    class Meta:
        verbose_name="Brand"
        verbose_name_plural="Brands"
        
    def __str__(self) -> str:
        return self.name   

class TagsModel(models.Model):
    tag=models.CharField( max_length=15)
    
    def __str__(self):
        return self.tag 
    
class ProductModel(models.Model):
    brand           =models.ForeignKey(BrandModel, on_delete=models.CASCADE, null=True)
    category        =models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    tags            =models.ManyToManyField(TagsModel)
    product_name    =models.CharField(unique=True, max_length=50)
    price           =models.DecimalField(max_digits=8, decimal_places=2)
    stock           =models.IntegerField()
    description     =models.TextField(max_length=255)
    is_avalible     =models.BooleanField(default=True)
    created_date    =models.DateTimeField( auto_now_add=True)
    updated_date    =models.DateTimeField(auto_now=True)
    image           =models.ImageField(upload_to="uploads/product")
    slug            =models.SlugField(unique=True, max_length=100)
    is_trending     =models.BooleanField(default=False)    
    discount_percent=models.IntegerField(null=True, default=0)
    category_trending=models.BooleanField(default=False)
    
        
    WARRANTY_CHOICES = [
    ('month', 'Month'),
    ('year', 'Year'),
    ]

    warranty = models.CharField(
        max_length=5, 
        choices=WARRANTY_CHOICES,
        default='month' 
    )   
    warranty_duration = models.IntegerField(default=1)
    
    def save(self, *args, **kwargs):
        if self.category_trending:
            ProductModel.objects.filter(category=self.category, category_trending=True).exclude(pk=self.pk).update(category_trending=False)
        super(ProductModel, self).save(*args, **kwargs)
        
    def discounted_price(self):
        if self.discount_percent is not None and self.discount_percent > 0:
            discount_amount = (Decimal(self.discount_percent) / 100) * self.price
            discounted_price = self.price - discount_amount
            return discounted_price.quantize(Decimal('0.00'))
        else:
            return self.price.quantize(Decimal('0.00'))
     
    def averageReview(self):
        reviews=ProductReview.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg=0
        if reviews['average'] is not None:
            avg=float(reviews['average'])
        return avg            
    
    def countReview(self):
        reviews=ProductReview.objects.filter(product=self, status=True).aggregate(count=Count('rating'))
        count=0
        if reviews['count'] is not None:
            count=int(reviews['count'])
        return count
           
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
              
    def __str__(self) -> str:
        return self.product_name
      
class ProductImagegallery(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="uploads/product", max_length=255)
    
    class Meta:
        verbose_name = "ProductImagegallery"
        verbose_name_plural = "Product Image gallery"
           
    def __str__(self):
        return self.product.product_name  
   
class Productfeatures(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    feature=models.CharField(max_length=50, default="no information provided")
    
    class Meta:
        verbose_name = "Productfeatures"
        verbose_name_plural = "Product features"
        
    def __str__(self):
        return self.product.product_name
      
class ProductPageDescription(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="uploads/productdescription", max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name = "ProductPageDescription"
        verbose_name_plural = "Product Page Description"
        
    def __str__(self):
        return self.product.product_name
        
class ProductReview(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    # user=models.ForeignKey(Account, on_delete=models.CASCADE)
    subject=models.CharField( max_length=100, blank=True)
    review=models.TextField(blank=True, max_length=500)
    rating=models.FloatField()
    ip=models.CharField( max_length=30, blank=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.first_name
    
class ExclusivePromotions(models.Model):
    # duration=models.OneToOneField(PromotionDuration, verbose_name=("duration"), on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    
    def clean(self):
        if ExclusivePromotions.objects.count() >= 5 and not self.pk:
            raise ValidationError('Only 5 products can be added to the promotions, and you have already added 5 products to promotions please delete some.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ExclusivePromotions, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.product_name   

def validate_image_extension(value):
    if not value.name.endswith('.png'):
        raise ValidationError('Only PNG files are allowed.')

class BanerAdds(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    banner_image=models.ImageField(upload_to="uploads/Banneradd_background", max_length=255, null=True, blank=True)
    product_image = models.ImageField(upload_to="uploads/Banneradd_product", validators=[validate_image_extension])
    
        
    def __str__(self):
        return self.product.product_name