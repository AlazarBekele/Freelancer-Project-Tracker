from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as auth_user
from .models import (
    Welcome,
    GoInto,
    Profiles,
    Follow
)

from .forms import (
    Sign_up,
    Sign_in,
    noteform
)

from django.contrib.auth import login, logout, authenticate
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

    accountIMG = Welcome.objects.get (id=3)

    sign_up = Sign_up (request.POST)

    if request.method == 'POST':

        if sign_up.is_valid():

            sign_up.save()

            return redirect ('Index')
        
        else:

            return render (request, 'Include/Log/LoginPage.html', {'accountCreate' : accountIMG, 'signup' : sign_up})

    context = {

        'accountCreate' : accountIMG,
        'signup' : sign_up

    }

    return render (request, 'Include/Log/LoginPage.html', context=context)


@login_required (login_url='/login/')
def goto_pass (request):

    # User logged in account Fetch data
    user = request.user
    DashboardIMG = GoInto.objects.get(id=1)

    context = {

        'DashboardIMG' : DashboardIMG,
        'logged_data' : user

    }

    return render (request, 'Include/Goto/pass.html', context=context)

## MAIN PAGES (Freelancer's & Client's)
@login_required (login_url='/login/')
def freelancer_page (request, id):

    # Start Here Follow
    follow_info = Profiles.objects.exclude(user=request.user)

    # Followers Id
    followers_Profile = Profiles.objects.get(user=request.user)
    followers_id = followers_Profile.follow_suggetion.values_list('id', flat=True)
    
    img = Profiles.objects.filter(id__in=followers_id).exclude (user=request.user)

    # Followers Counter
    Follow.objects.get_or_create (followers=request.user)

    # Note
    notes = noteform (request.POST or None)

    if request.method == 'POST':

        if notes.is_valid():

            notes.save()
            return redirect ('Freelancers')

    # Load profile Picture
    if request.user.id == id:

        profile_img = Profiles.objects.get (id=id)

    elif request.user.id != id:

        return redirect ('Login')
    
    else:

        return redirect ('Index')

    user = request.user

    context = {
        'user' : user,
        'profile_img' : profile_img,
        'follow_info' : follow_info,
        'followers_id' : followers_id,
        'images' : img,
        'notes' : notes
    }

    if request.user.is_authenticated:

        return render (request, 'Pages/Freelancers/freelancer_page.html', context=context)
    
    else:

        return redirect ('Index')


@login_required (login_url='/login/')
def crud_info (request, username):

    user = request.user

    context = {
        'user_profile' : user
    }

    return render (request, 'Pages/Include/Edit Profile/CRUD.html', context=context)