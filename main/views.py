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
from main.models import Product, TopModel, NewModel, BlogPost, Brand
from django.contrib.auth.decorators import login_required

""" 
    Python file for loading pages and doing things related to loading
"""

def index(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    context["products"] = Product.objects.all()
    context["topmodel"] = TopModel.objects.all()
    context["newmodel"] = NewModel.objects.all()
    context["blogpost"] = BlogPost.objects.all()
    context["brand"] = Brand.objects.all()
    return render(request, "main_template/index.html", context)

def delivery(request):
    """ Function loading delivery page """
    context = {"current_user": request.user}
    return render(request, "dostavka.html", context)

def product(request, product_id):
    """ Function loading products on 'tavar' page """
    product_info = Product.objects.get(id=product_id)
    context = {"current_user": request.user}
    context["info"] = product_info
    return render(request, "product.html", context)

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
