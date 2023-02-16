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
from main.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

""" 
    Python file for loading pages and doing things related to loading
"""

def index(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    return render(request, "index.html", context)

def index_i(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    return render(request, "index.html", context)
def about_i(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    return render(request, "index.html", context)
def watches(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    return render(request, "index.html", context)
def contact(request):
    """ Function loading index page """
    context = {"current_user": request.user}
    return render(request, "index.html", context)



def cart(request):
    """ Function loading cart page """
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)

def info(request):
    """ Function loading info page """
    context = {"current_user": request.user}
    return render(request, "tmp_index.html", context)

def delivery(request):
    """ Function loading delivery page """
    context = {"current_user": request.user}
    return render(request, "dostavka.html", context)


def katalog(request):
    """ Function loading catalog page """
    context = {"current_user": request.user}
    context["products"] = Product.objects.all()
    return render(request, "katalog.html", context)


def product(request, product_id):
    """ Function loading products on 'tavar' page """
    product_info = Product.objects.get(id=product_id)
    context = {"current_user": request.user}
    context["info"] = product_info
    return render(request, "tovar.html", context)
'''

def user_login(request):
    """ Function for controlling authorization and loading login page"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'profile.html', {'section': 'dashboard'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'sign.html', {'form': form})

'''
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
def home(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    return redirect('login')

@login_required
def dashboard(request):
    """ Page loading dashboard """
    return render(request, 'profile.html', {'section': 'dashboard'})

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    context = {"current_user": request.user}
    cart.add(product, product.price)
    return render(request, "korzina.html", context)


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)


@login_required
def cart_detail(request):
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)

def contacts(request):
    """ Function loading contacts page """
    context = {"current_user": request.user}
    return render(request, "contacts.html", context)