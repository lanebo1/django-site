from django.contrib import admin
from .models import Product, ProductImage, TopModel, BlogPost, Brand, ProductPoint


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
class ProductPointAdmin(admin.StackedInline):
    model = ProductPoint

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductPointAdmin]
    class Meta:
        model = Product
@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductPoint)
class PostPointAdmin(admin.ModelAdmin):
    pass

admin.site.register(TopModel)
admin.site.register(BlogPost)
admin.site.register(Brand)