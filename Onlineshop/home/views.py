from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, "home/index.html", {})


def home(request):
    return render(request, "home/index.html", {})

def user_login(request):
    context ={}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reversed("success"))
        else:
            context["error"] = "provide valid credential !!"
            return render(request, "home/login.html", context)
    return render(request, "home/login.html", context)

def success(request):
    pass

def logout(request):
    pass
def checkout(request):
    return render(request, "home/checkout.html", {})

def cart(request):
    return render(request, "home/cart.html", {})

