from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.models import Product, TopModel, BlogPost, Brand, ProductImage, ProductPoint
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode
""" 
    Python file for loading pages and doing things related to loading
"""

def index(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    context["products"] = Product.objects.all()
    context["topmodel"] = TopModel.objects.all()
    context["blogpost"] = BlogPost.objects.all()
    context["brand"] = Brand.objects.all()
    return render(request, "main_template/index.html", context)

def delivery(request):
    """ Function loading delivery page """
    context = {"current_user": request.user}
    return render(request, "dostavka.html", context)

def product(request, product_id):
    """ Function loading products on 'tavar' page """
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)
    context = {"current_user": request.user}
    context['product'] = product
    context['images'] = images
    return render(request, "main_template/product.html", context)
"""
def out(request, product_id):
    query_string = urlencode({'product_id': product_id})  # 2 category=42
    url = '{}{}'.format('/checkout/', product_id)  # 3 /products/?category=42
    if request.user.is_authenticated:
        return redirect(url)  # 4
    else:
        url = '{}{}'.format('/reigester/', product_id)  # 3 /products/?category=42
        return redirect(url)  # 4
def checkout(request, product_id):
    if not request.path == reverse(out):
        return render(request, "main_template/blog.html")
"""
def blog(request, blog_id):
    """ Function loading products on 'tavar' page """
    blog = BlogPost.objects.get(id=blog_id)
    context = {"current_user": request.user}
    context['blog'] = blog
    return render(request, "main_template/blog.html", context)

def exit(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)
    points = ProductPoint.objects.filter(product=product)
    context = {"current_user": request.user}
    context['product'] = product
    context['images'] = images
    context['points'] = points
    return render(request, "main_template/checkout.html", context)

def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = SignUpForm()

    return render(request, "register.html", {"form": form, "msg": msg, "success": success})
# Login
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None
    if request.method == "POST":

        if form.is_valid():
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid credentials.')
        else:
            messages.error(request, 'Error validating the form.')
    return render(request, "login.html", {"form": form, "msg": msg})

@login_required
def dashboard(request):
    """ Page loading dashboard """
    return render(request, 'profile.html', {'section': 'dashboard'})
