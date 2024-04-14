from django.urls import path
from home import views
from feature import views as feature_view

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("about",feature_view.about,name="about"),
    path("resource",feature_view.resource,name="resource"),
    path("team",feature_view.team,name="team"),
    path("blog",feature_view.blog,name="blog"),
    path("blogview",feature_view.blogview,name="blogview"),
    path("gallery",feature_view.gall,name="gallery"),
    path("event",feature_view.event,name="event"),
    path("contact",feature_view.contact,name="contact"),
]
