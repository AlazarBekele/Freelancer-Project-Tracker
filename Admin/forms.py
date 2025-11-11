from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_up (UserCreationForm):

    first_name = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'First Name'

    }))

    last_name = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'Last Name'

    }))

    username = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'username'

    }))

    email = forms.EmailField (label='' ,widget=forms.EmailInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'username'

    }))

    password1 = forms.CharField (max_length=10,label='' , widget=forms.PasswordInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'username'

    }))

    password2 = forms.CharField (max_length=10,label='' , widget=forms.PasswordInput(attrs={

        'class' : 'w-120',
        'placeholder' : 'username'

    }))

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')