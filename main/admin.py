from django.contrib import admin
from .models import Product, TopModel, NewModel, BlogPost, Brand

admin.site.register(Product)
admin.site.register(TopModel)
admin.site.register(NewModel)
admin.site.register(BlogPost)
admin.site.register(Brand)