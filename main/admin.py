from django.contrib import admin
from .models import Product, ProductImage, TopModel, NewModel, BlogPost, Brand


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    class Meta:
        model = Product
@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(TopModel)
admin.site.register(NewModel)
admin.site.register(BlogPost)
admin.site.register(Brand)