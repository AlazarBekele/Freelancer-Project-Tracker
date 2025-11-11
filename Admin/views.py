from django.shortcuts import render
from .models import (
    Welcome
)

# Create your views here.

def index (request):

    WelIMG = Welcome.objects.all()

    context = {

        'welcomeIMG' : WelIMG

    }

    return render (request, 'index.html', context=context)


def loginPage (request):

    accountIMG = Welcome.objects.get (id=2)

    context = {

        'accountCreate' : accountIMG

    }

    return render (request, 'Include/Log/LoginPage.html', context=context)