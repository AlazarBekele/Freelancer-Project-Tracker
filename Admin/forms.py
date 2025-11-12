from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_up (UserCreationForm):

    ROLE_CHOOES = [
        ('client', 'Client'),
        ('freelancer', 'Freelancer')
    ]

    field_choose = forms.ChoiceField (choices=ROLE_CHOOES, label='Freelancer or Client', widget=forms.Select(attrs={

        'class' : 'w-full border-none focus:outline-none p-3 bg-white rounded-md',

    }))

    first_name = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-70 border-none focus:outline-none p-3 bg-white rounded-md',
        'placeholder' : 'First Name'

    }))

    last_name = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-70 border-none focus:outline-none p-3 bg-white rounded-md',
        'placeholder' : 'Last Name'

    }))

    username = forms.CharField (max_length=20,label='' , widget=forms.TextInput(attrs={

        'class' : 'w-full border-none focus:outline-none p-3 bg-white rounded-md',
        'placeholder' : 'username'

    }))

    email = forms.EmailField (label='' ,widget=forms.EmailInput(attrs={

        'class' : 'w-full border-none focus:outline-none p-3 bg-lime-200/40 rounded-md',
        'placeholder' : 'Email'

    }))

    password1 = forms.CharField (max_length=10,label='' , widget=forms.PasswordInput(attrs={

        'class' : 'w-70 border-none focus:outline-none p-3 bg-white rounded-md',
        'placeholder' : 'Password'

    }))

    # password2 = forms.CharField (max_length=10,label='' , widget=forms.PasswordInput(attrs={

    #     'class' : 'w-70 border-none focus:outline-none p-3 bg-white rounded-md',
    #     'placeholder' : 'Confirm Password'

    # }))

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'field_choose')