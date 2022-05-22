from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import debug_toolbar


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    path('remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]