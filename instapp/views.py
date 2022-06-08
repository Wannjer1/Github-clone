from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# this imports the  pre-built Django form logging in a user.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import *
# authentication
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from django.urls import reverse



# Create your views here.
# registration view function
def home(request):
    return render (request, 'insta/index.html')

@login_required()
def profile(request):
    profile=Profile.objects.all()
    return render(request, 'insta/profile.html',{'profile': profile})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    
    return render (request, "insta/register.html", context={"form":form})

# login view function
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render (request, 'insta/login.html', context={"login_form": form})



