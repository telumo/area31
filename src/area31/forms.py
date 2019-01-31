from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    pass

class ProfileForm(forms.ModelForm):
    username = forms.CharField(help_text='必須項目です。')
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('gender', 'grad_year', 'class_of', 'image' ) 