from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#Routes URLs with views.py, so you have to use @login_required(login_url='login'), instead of @login_required(login_url='index.html')


#I removed this comment, misplaced and was meant for my .html file, the comment was for when I couldn't figure out how to change my hyperlinks from html to django format. I used a w3schools link, but it didnt work, it was php not python.
#Replaced

urlpatterns = [
    #You have to add views. for the views.py function
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('post_list/', views.post_list, name='post_list'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('resources/', views.resources, name='resources'),
    path('topics/', views.topics, name='topics'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/index.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
