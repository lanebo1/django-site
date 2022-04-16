from django.contrib import admin
from .models import Product, Category, Creator

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Creator)
