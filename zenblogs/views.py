from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def category(request):
    return render(request, 'category.html')
def single_post(request):
    return render(request, 'single-post.html')
def starter_page(request):
    return render(request, 'starter-page.html')
