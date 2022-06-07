from django.contrib.auth.forms import AuthenticationForm
# this imports the  pre-built Django form logging in a user.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
# registration view function

def register(request):
    return render (request, 'insta/register.html')

# login view function
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('insta/home.html')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render (request=request, template_name='insta/login.html', context={"login_form": form})

def home(request):
    return render (request, 'insta/index.html')

