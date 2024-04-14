from django.shortcuts import render
from django.shortcuts import redirect
from home.models import schoolnums,investor,homePageImage

# Create your views here.
def index(request):
    indexHead=schoolnums.objects.first()
    investors=investor.objects.all()
    homeimage=homePageImage.objects.all()
    context={
        'indexHead':indexHead,
        'investors':investors,
        'homeimages':homeimage,
    }
    return render(request,"core/index.html",context)
