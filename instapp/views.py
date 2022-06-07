from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
# registration view function

def register(request):
    return render (request, 'insta/register.html')

def home(request):
    return render (request, 'insta/index.html')

