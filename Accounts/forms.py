from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import AccountInfo

User = get_user_model()

class Sign_up (UserCreationForm):

    # ROLE_CHOOES = [
    #     ('client', 'Client'),
    #     ('freelancer', 'Freelancer')
    # ]

    # WORK_ON = [
    #     ('Website', 'Website'),
    #     ('Video Editor', 'Video Editor'),
    #     ('Account Finace', 'Account Finace'),
    #     ('Website Design', 'Website Design'),
    #     ('Human Resource', 'Human Resource'),
    #     ('Software Engineering', 'Software Engineering'),
    # ]

    field_choose = forms.ChoiceField (label='Freelancer or Client', widget=forms.Select(attrs={

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

    username = forms.CharField (max_length=10,label='' , widget=forms.TextInput(attrs={

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

    password2 = forms.CharField (max_length=10,label='' , widget=forms.PasswordInput(attrs={

        'class' : 'w-70 border-none focus:outline-none p-3 bg-white rounded-md',
        'placeholder' : 'Confirm Password'

    }))

    working_fields = forms.ChoiceField (label='Choose Your Field', widget=forms.Select(attrs={

        'class' : 'w-full border-none focus:outline-none p-3 bg-white rounded-md',

    }))

    class Meta:

        model = AccountInfo
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'field_choose', 'password2', 'working_fields')

    # def save(self, commit=True):

    #     user = super().save(commit=False)
    #     user.field_choose = self.cleaned_data['field_choose']
    #     user.working_fields = self.cleaned_data['working_fields']

    #     if commit:

    #         user.save()

    #     return user
    

class Sign_in (forms.Form):

    username = forms.CharField (max_length=30, widget=forms.TextInput(attrs={

        'class' : 'text-lime-600 focus:outline-none border-b-1 border-lime-500 placeholder:text-lime-600/40 placeholder:font-thin px-3',
        'placeholder' : "Username"

    }))

    password = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={

        'class' : 'text-lime-600 focus:outline-none border-b-1 border-lime-500 placeholder:text-lime-600/40 placeholder:font-thin px-3',
        'placeholder' : "Password"

    }))