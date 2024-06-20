from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#I had trouble figuring out how to add the links to other webpages
#Ended up looking at the resource on https://www.w3schools.com/django/django_add_link_details.php
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
