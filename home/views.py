from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def about(request):
    return render(request,"core/about.html")

def resource(request):
    return render(request,"core/resource.html")

def team(request):
    return render(request,"core/team.html")

def blog(request):
    return render(request,"core/blog.html")

def gallery(request):
    return render(request,"core/gallery.html")

def event(request):
    return render(request,"core/event.html")

def contact(request):
    return render(request,"core/contact.html")
