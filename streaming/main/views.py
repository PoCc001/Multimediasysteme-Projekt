from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request)
            return redirect("/streaming")
        else:
            return render(request, "login.html", {'error': True})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordconf = request.POST.get("passwordconf")

        if password != passwordconf:
            return render(request, "register.html", {"error": "password"})
        
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('/streaming')

    else:
        return render(request, "register.html")

@login_required(login_url="/login")
def streaming(request):
    return render(request, "streaming.html")

@login_required(login_url="/login")
def settings(request):
    return render(request, "settings.html")



