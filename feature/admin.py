from django.contrib import admin
from feature.models import events,gallery,teamMembers,aboutUs,blog

# Register your models here.
admin.site.register(blog)
admin.site.register(aboutUs)
admin.site.register(teamMembers)
admin.site.register(gallery)
admin.site.register(events)