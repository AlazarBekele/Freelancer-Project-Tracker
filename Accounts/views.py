from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as auth_user
from django.shortcuts import get_object_or_404

from .models import (
    Welcome,
    GoInto,
    Profiles,
    Follow,
    Publish_Page_Model
)

from .forms import (
    Sign_up,
    Sign_in,
    noteform,
    Publish_form
)

from django.db.models import F

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

    # If the user is auth... no login again
    if request.user.is_authenticated:
        return redirect ('Pass')
    
    else:
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
def freelancer_page (request, id, username):

    profile = request.user.profile

    # Start Here Follow , --> Give All profile except mine
    follow_info = Profiles.objects.exclude(user=request.user)

    # Followers Id
    followers_id = profile.follow_suggetion.values_list('id', flat=True)
    img = Profiles.objects.filter(id__in=followers_id).exclude (user=request.user)

    # Followers Counter
    Follow.objects.get_or_create (followers=request.user)

    # -> Start Displaying the Post form Latest - Oldest
    Displaying = Publish_Page_Model.objects.order_by('-create_info')

    # Get Publisher Profile Data
    post_id = request.GET.get ('post_id')

    # View Increament IF
    if post_id:
        post = get_object_or_404 (Publish_Page_Model, id=post_id)
        session_key = f'Viewed_post{post.id}'

        if not request.session (session_key):
            post.increment_views()
            request.session[session_key] = True

        post.refresh_from_db()

    # Share note For Site
    if request.method == 'POST':
        forms_note = noteform (request.POST, request.FILES, instance=profile)
        if forms_note.is_valid ():
            forms_note.save()

    else:
        forms_note = noteform (instance=profile)


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
        'forms_note' : forms_note,
        'profile' : profile,
        'Displaying' : Displaying
    }

    if request.user.is_authenticated:
        return render (request, 'Pages/Freelancers/freelancer_page.html', context=context)
    
    else:
        return redirect ('Index')
    

# def post_detail (request, post_id):

#     post = get_object_or_404 (Publish_Page_Model, id=post_id)
    
#     session_key = f'viewed_post_{post.id}'

#     if not request.session.get(session_key):
#         Publish_Page_Model.objects.filter (id=post_id).update (
#             views=F('View') + 1
#         )

#         request.session[session_key] = True
#         post.refresh_from_db()


def logout_session (request):
    
    #logout Handle
    if request.method == 'POST':
        logout (request)
        return redirect ('Index')
    
    return render (request, 'Pages/Include/Freelancers Category/navbar.html')


@login_required (login_url='/login/')
def crud_info (request, username):

    user = request.user

    context = {
        'user_profile' : user
    }

    return render (request, 'Pages/Include/Edit Profile/CRUD.html', context=context)


@login_required (login_url='/login/')
def publish_page_both (request, username):

    PublishForm = Publish_form (request.POST, request.FILES)
    profile = Profiles.objects.get(user = request.user)

    if request.method == 'POST':

        if PublishForm.is_valid():

            obj = PublishForm.save(commit=False)
            obj.profile = profile
            obj.save()
            return redirect ('Pass')
    
    context = {
        'Publish_Form_Context' : PublishForm
    }

    return render (request, 'Pages/Publish/Publish.html', context=context)