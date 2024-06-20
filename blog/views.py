from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import  authenticate

#https://stackoverflow.com/questions/11241080/django-contrib-auth-logout-in-django
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    form = AuthenticationForm()
    return render(request, 'blog/index.html', {'form': form})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'Good job you have successfully signed up for my blog')
        else:
            messages.error(request, "You didn't follow the instructions")
    return render(request, 'blog/signup.html', {'form': form})

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def topics(request):
    return render(request, 'blog/topics.html', {})

def aboutme(request):
    return render(request, 'blog/aboutme.html', {})

def resources(request):
    return render(request, 'blog/resources.html', {})

#Custom logout_view taken from stack overflow
def logout_view(request):
    logout(request)
    return redirect('index')