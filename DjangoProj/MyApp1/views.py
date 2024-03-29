from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher
from .models import asset



# Create your views here.
def index(request):
    teach = teacher.objects.all() 
    return render(request,"MyApp1/index.html",{'content': teach})



def asset(request):
    return render(request, 'MyApp1/assetlist.html') 
