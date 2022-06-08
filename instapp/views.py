from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# this imports the  pre-built Django form logging in a user.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import *
from django.urls import reverse
from .email import send_welcome_email
from email import message
from email.mime import image
from django.core.mail import send_mail
from django.conf import settings
# authentication
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from django.urls import reverse





# Create your views here.
#home function that displayes all posts
def home(request):
    pictures = Image.objects.all()

    return render(request, 'insta/index.html', {'pictures': pictures,}) 


# comment view function
def comment(request,image_id):
    comment=Comment.objects.all()
    post=Image.objects.get(id=image_id)
    if request.method == 'POST':
        form=CommentForm(request.POST )
        if form.is_valid():
            form=form.save(commit=False)
            form.post=post
            form.save()
            return redirect('home')
    else:
        form=CommentForm()
    return render(request, 'comments.html',{'comment':comment,'form':form,'post':post})

# profile function
@login_required()
def profile(request):
    profile=Profile.objects.all()
    return render(request, 'insta/profile.html',{'profile': profile})

# authentication
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
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render (request, 'insta/login.html', context={"login_form": form})

# register view function
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
            # username=request.POST['username']
            # email=request.POST['email']
            # subject='welcome to InstaApp'
            # message=f'Hi {username} welcome to InstaApp and have fun! '
            # from_email=settings.EMAIL_HOST_USER
            # recipients=[email]
            # send_mail(subject, message,from_email,recipients,fail_silently=False)

			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "insta/register.html", context={"register_form":form})

# logout view function
def logout(request):
    logout(request)

    return render (request, 'insta/logout.html')