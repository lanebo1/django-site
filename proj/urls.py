"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
import debug_toolbar


urlpatterns = [
    path('cart/', include('cartx.urls')),

    path('product/<int:product_id>', views.product, name='tovar'),
    path('',views.index, name='index'),
    path('katalog/',views.katalog, name='katalog'),
    path('delivery/', views.delivery),
    path('info/', views.info),
    path('contacts/', views.contacts),
    path('admin/', admin.site.urls),
    #path('/relogin/', django.contrib.auth.views.logout_then_login, name='relogin'),
    path('profile/', views.dashboard, name='profile'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path('home/', views.home, name="home"),
    path('index_i/', views.index_i, name="home"),
    path('watches/', views.watches, name="home"),
    path('about/', views.about_i, name="home"),
    path('contact/', views.contact, name="home"),

]

urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
