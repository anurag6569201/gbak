from django.shortcuts import render
from feature.models import aboutUs,teamMembers,gallery
# Create your views here.

def about(request):
    about=aboutUs.objects.first()
    context={
        'about':about,
    }
    return render(request,"core/about.html",context)

def resource(request):
    return render(request,"core/resource.html")

def team(request):
    team=teamMembers.objects.all()
    context={
        'team':team,
    }
    return render(request,"core/team.html",context)

def blog(request):
    return render(request,"core/blog.html")

def gall(request):
    galleryImages=gallery.objects.all()
    context={
        'galleryImages':galleryImages,
    }
    return render(request,"core/gallery.html",context)

def event(request):
    return render(request,"core/event.html")

def contact(request):
    return render(request,"core/contact.html")

def blogview(request):
    return render(request,"core/blog-single.html")
