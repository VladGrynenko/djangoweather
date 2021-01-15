
from django.shortcuts import render

# Create your views here.

#this is my home page view
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
