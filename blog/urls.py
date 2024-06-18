from django.urls import path
from . import views


#I had trouble figuring out how to add the links to other webpages
#Ended up looking at the resource on https://www.w3schools.com/django/django_add_link_details.php
#Replaced
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('resources/', views.resources, name='resources'),
    path('topics/', views.topics, name='topics'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]