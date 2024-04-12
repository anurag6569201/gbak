from django.contrib import admin
from home.models import homePageImage,investor,schoolnums

# Register your models here.
admin.site.register(schoolnums)
admin.site.register(investor)
admin.site.register(homePageImage)