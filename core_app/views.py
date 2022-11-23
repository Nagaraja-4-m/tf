from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.
from .models import *

def index(request):
    context={
        'products':ProductCard.objects.all()
        }
    # print(static)
    return render(request,'base.html',context)