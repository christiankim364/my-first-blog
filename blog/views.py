from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import  authenticate

#requires login to access separate forms of the website
#https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
from django.contrib.auth.decorators import login_required

#https://stackoverflow.com/questions/11241080/django-contrib-auth-logout-in-django
from django.contrib.auth import logout
from django.shortcuts import redirect

#https://www.youtube.com/watch?v=69Mb5yk-q8o
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


#I'm a little confused, I can't directly type in https://ckim73.pythonanywhere.com/post_list/ when I run the website locally using "python manage.py runserver", but when I commit to github, and run it on pythonanywhere.com, I can still bypass the login process...
#https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
@login_required(login_url='login') #redirects to the index login page, if you someone just tries to type in "http://127.0.0.1:8000/post_list/", without signing in
def post_list(request):
    return render(request, 'blog/post_list.html', {})

@login_required(login_url='login')
def topics(request):
    return render(request, 'blog/topics.html', {})

@login_required(login_url='login')
def aboutme(request):
    return render(request, 'blog/aboutme.html', {})

@login_required(login_url='login')
def resources(request):
    return render(request, 'blog/resources.html', {})

#Custom logout_view taken from stack overflow
def logout_view(request):
    logout(request)
    return redirect('index')