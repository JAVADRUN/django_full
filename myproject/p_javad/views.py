from django.shortcuts import render
from .models import Mobile_Article
# Create your views here.

def mobile(request):
    context = {
       'mobile': Mobile_Article.objects.all()
    }
    return render(request , "p_javad/mobile.html" , context)

def id_mobile(request , slug):
    context = {
        'mobiless' : Mobile_Article.objects.get(slug = slug)

    }    
    return render(request , "p_javad/detail.html" , context)