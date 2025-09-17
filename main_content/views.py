from django.shortcuts import render,redirect
from .forms import ContactForm
from .forms import MyForm
from django.conf import settings
import os
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    return render(request, 'main_content/index.html')

def about(request):
    return render(request, 'main_content/about.html')

def services(request):
    return render(request, 'main_content/services.html')

def highlights(request):
    return render(request, 'main_content/highlights.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContactForm()
    return render(request, 'main_content/contact.html', {
        "form": form,
    })

def projects(request):
    return render(request, 'main_content/projects.html')

# 

def dashboards(request):
    form = MyForm()
    if request.method == 'POST':
        # Process form submission here
        pass
    return render(request, 'main_content/dashboard.html', {'form': form})


def load_static_data():
    """Load the static JSON data from a file."""
    file_path = os.path.join(settings.BASE_DIR, 'data.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def is_ajax(request):
    """Check if a request is an AJAX request."""
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def blog(request):
    data = load_static_data()

    if is_ajax(request) and request.method == 'GET':
        category_name = request.GET.get('category')
        selected_category = next((cat for cat in data if cat['category'] == category_name), None)
        if selected_category:
            return JsonResponse(selected_category['subcategories'], safe=False)

    
    if is_ajax(request) and request.method == 'POST':
        subcategory_id = request.POST.get('subcategory_id')
        for category in data:
            subcategory = next((sub for sub in category['subcategories'] if sub['id'] == int(subcategory_id)), None)
            if subcategory:
                return JsonResponse(subcategory['formFields'], safe=False)

    # Render the page with the categories
    return render(request, 'main_content/blog.html', {'categories': data})
    
    # return render(request, 'main_content/blog.html')