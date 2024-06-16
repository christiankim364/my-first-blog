from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def aboutme(request):
    return render(request, 'blog/aboutme.html', {})

def resources(request):
    return render(request, 'blog/resources.html', {})

def topics(request):
    return render(request, 'blog/topics.html', {})