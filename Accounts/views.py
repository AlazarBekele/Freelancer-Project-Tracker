from django.shortcuts import render, redirect
from .models import (
    Welcome,
    GoInto,
    Profiles,
    Work_fields
)

from .forms import (
    Sign_up,
    Sign_in,
    Work_flow
)

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .signals import create_profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):

    form = Sign_in (request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate (request, username=username, password=password)

            if user is not None:

                login (request, user)

                return redirect ('Pass')

    WelIMG = Welcome.objects.get (id=1)

    context = {

        'welcomeIMG' : WelIMG,
        'form' : form

    }

    return render (request, 'index.html', context=context)


def loginPage (request):

    accountIMG = Welcome.objects.get (id=4)

    sign_up = Sign_up (request.POST or None)

    if request.method == 'POST':

        if sign_up.is_valid():

            role = sign_up.cleaned_data.get('role')

            user = sign_up.save(commit=False)

            user.field_choose = sign_up.cleaned_data.get('field_choose')

            user.save()

            return redirect ('Index')

    context = {

        'accountCreate' : accountIMG,
        'signup' : sign_up

    }

    return render (request, 'Include/Log/LoginPage.html', context=context)

# Set out the Extracted data
# def client_dashboard (request):

#     if request.user.profile.role != 'client':

#         return redirect ("No_permission")

#     return render (request, '')

@login_required (login_url='/login/')
def goto_pass (request):

    # User logged in account Fetch data
    user = request.user
    DashboardIMG = GoInto.objects.get(id=1)

    # user_work_info = Work_fields.

    if request.method == "POST":

        form = Work_flow (request.POST, request.FILES)

        if form.is_valid():

            # Recive cleaned data form forms.py
            user_work_info = form.cleaned_data['working_fields']

            # Using create method save the datas got form ther

            user_model_date = Work_fields.objects.create (

                user_info = user_work_info

            )

            user_model_date.save()
            messages.success (request, 'The Data Is Saved.')
            return redirect ('Freelancers')
        
    
    context = {

        'DashboardIMG' : DashboardIMG,
        'logged_data' : user,
        'work_flow' : work_flow

    }

    return render (request, 'Include/Goto/pass.html', context=context)

## MAIN PAGES (Freelancer's & Client's)

def freelancer_page (request):

    user = request.user

    context = {
        'user' : user
    }

    if request.user.is_authenticated:

        return render (request, 'Pages/Freelancers/freelancer_page.html', context=context)
    
    else:

        return redirect ('Index')