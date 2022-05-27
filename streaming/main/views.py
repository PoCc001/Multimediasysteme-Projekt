from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def streaming(request):
    return render(request, "streaming.html")

def settings(request):
    return render(request, "settings.html")



