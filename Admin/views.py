from django.shortcuts import render, redirect
from .models import (
    Welcome
)

from .forms import (
    Sign_up
)

# Create your views here.

def index (request):

    WelIMG = Welcome.objects.get (id=1)

    context = {

        'welcomeIMG' : WelIMG

    }

    return render (request, 'index.html', context=context)


def loginPage (request):

    accountIMG = Welcome.objects.get (id=2)

    sign_up = Sign_up (request.POST or None)

    if request.method == 'POST':

        if sign_up.is_valid():

            sign_up.save()
            return redirect ('login')
        else:

            print (sign_up.errors)

    context = {

        'accountCreate' : accountIMG,
        'signup' : sign_up

    }

    return render (request, 'Include/Log/LoginPage.html', context=context)