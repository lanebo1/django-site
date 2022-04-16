from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def index(request):
    context = {"current_user": request.user}
    return render(request, "index.html", context)


def cart(request):
    context = {"current_user": request.user}
    return render(request, "korzina.html", context)


def delivery(request):
    context = {"current_user": request.user}
    return render(request, "dostavka.html", context)


def katalog(request):
    context = {"current_user": request.user}
    context["products"] = Product.objects.all()
    return render(request, "katalog.html", context)


def product(request, product_id):
    product_info = Product.objects.get(id=product_id)
    context = {"current_user": request.user}
    context["info"] = product_info
    return render(request, "tavar.html", context)

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            login(request, new_user)
            #messages.success(request, "Успешно")
            return redirect("/")
        else:
            return render(request, "registration/signup.html", {'user_form': user_form})
    else:
        user_form = UserCreationForm()
        return render(request, 'registration/signup.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'relogin.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
