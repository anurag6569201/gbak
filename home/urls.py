from django.urls import path
from home import views

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("causes",views.causes,name="causes"),
    path("donate",views.donate,name="donate"),
    path("blog",views.blog,name="blog"),
    path("gallery",views.gallery,name="gallery"),
    path("event",views.event,name="event"),
    path("contact",views.contact,name="contact"),
]
