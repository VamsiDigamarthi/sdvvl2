from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main_content/index.html')

def about(request):
    return render(request, 'main_content/about.html')

def services(request):
    return render(request, 'main_content/services.html')

def highlights(request):
    return render(request, 'main_content/highlights.html')