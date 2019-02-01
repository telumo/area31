from .models import Profile, Location, LocationLabel
from django.contrib.auth.models import User
from django import forms
# from django.contrib.auth.forms import UserCreationForm

class LocationRegisterForm(forms.ModelForm):

    # user = forms.CharField()

    latitude = forms.CharField(
        label='latitude',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'latitude',
                'value' : '',
                'name' : 'latitude',
                'readonly' : 'readonly'
            }
        )
    )

    longitude = forms.CharField(
        label='longitude',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'longitude',
                'value' : '',
                'name' : 'longitude',
                'readonly' : 'readonly'
            }
        )
    )

    label = forms.ModelChoiceField(
        label='場所のラベル',
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'selectpicker',
                'data-style' : 'select-with-transition',
                'title' : 'Choose Location Label',
                'data-size' :'7',
                'name' : 'label'
            }
        ), 
        queryset=LocationLabel.objects.all()
    )

    class Meta:
        model = Location
        fields = ("latitude", "longitude", "label",)


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(
        label='名',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    
    last_name = forms.CharField(
        label='姓',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)

class ProfileForm(forms.ModelForm):
    
    gender = forms.ChoiceField(
        label='性別',
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'selectpicker',
                'data-style' : 'select-with-transition',
                'title' : 'Gender',
                'data-size' :'7'
            }
        ), 
        choices=Profile.GENDER_CHOICES
    )

    image = forms.ImageField(required=False)

    grad_year = forms.ChoiceField(
        label='卒業年',
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'selectpicker',
                'data-style' : 'select-with-transition',
                'title' : 'Graduation Year',
                'data-size' :'7'
            }
        ), 
        choices=Profile.GRAD_YEARS
    )

    class_of = forms.ChoiceField(
        label='期',
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'selectpicker',
                'data-style' : 'select-with-transition',
                'title' : 'the Class',
                'data-size' :'7'
            }
        ), 
        choices=Profile.CLASS_OF
    )

    about_me = forms.CharField(
        label='姓',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'rows' : '5'
            }
        )
    )

    image = forms.ImageField(
        label='プロフィール画像',
        required=False,
        # upload_to='image/',
        # verbose_name='添付画像',
        # height_field='url_height',
        # width_field='url_width',
        # default='assets/img/default-avatar.png'

    )

    class Meta:
        model = Profile
        fields = ('gender', 'grad_year', 'class_of', 'about_me', 'image',  ) 