from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Profile,Image,Comment

# registration form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'bio','profile_photo']

        labels={
            'name':'name',
            'username':'username',
            'profile_photo':'photo',
            'bio':'bio',
        }

        widgets={
           'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name '}),
           'username':forms.TextInput(attrs={'class': 'form-control','placeholder':' username'}),
           
           'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'bio'}),
          
        }


# comment form
class CommentForm(ModelForm):
    class Meta:
        model= Comment
        # fields= "__all__"
        fields=('comment',   )

        labels={
            'comment':'',

        }

        widgets={
           'comment': forms.TextInput(attrs={'placeholder':' post a comment '}),
        }

