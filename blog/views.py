from django.shortcuts import render
#Added this https://tutorial.djangogirls.org/en/extend_your_application/
from . import views

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def topics(request):
    return render(request, 'blog/topics.html', {})

def aboutme(request):
    return render(request, 'blog/aboutme.html', {})

def resources(request):
    return render(request, 'blog/resources.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def signup(request):
    return render(request, 'blog/signup.html', {})

