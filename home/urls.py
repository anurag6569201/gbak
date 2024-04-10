from django.urls import path
from home import views

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("resource",views.resource,name="resource"),
    path("team",views.team,name="team"),
    path("blog",views.blog,name="blog"),
    path("gallery",views.gallery,name="gallery"),
    path("event",views.event,name="event"),
    path("contact",views.contact,name="contact"),
]
