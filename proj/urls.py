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
import debug_toolbar


urlpatterns = [
    path('',views.index, name='index'),
    path('katalog/',views.katalog, name='katalog'),
    path('product/<int:product_id>', views.product, name='tovar'),
    path('delivery/', views.delivery),
    path('cart/', views.cart),
    path('info/', views.info),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('/relogin/', django.contrib.auth.views.logout_then_login, name='relogin'),
    path('profile/', views.dashboard, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='registr')

]

urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
