from django.shortcuts import render

# Create your views here.
def landng(request):
    return render(request,"landng.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")


