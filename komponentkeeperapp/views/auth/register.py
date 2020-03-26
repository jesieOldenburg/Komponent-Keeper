from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from komponentkeeperapp.models import Creator
from django.views.decorators.csrf import csrf_exempt

def register_user(request):
    """View method for handling creation of a new user for auth

        Args:
        request = full http object
    """

    if request.method == 'GET':
        creator = Creator.objects.all()

        template = 'registration/register.html'
        context = {
            'creators': creator
        }

        return render(request, template, context)

    # For handling when user submits the form data
    if request.method == "POST":
        # Create the instance of a new AUTH_USER
        form_data = request.POST
        new_user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=form_data['password'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )
        # Then store that AUTH_USER object inside of creator
        creator = Creator.objects.create(
            user=new_user,
        )
        new_user = authenticate(username=form_data['username'], password=form_data['password'])
        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
    return redirect(reverse('komponentkeeperapp:components'))

    # handles a request to load the empty form for the useer to fill out
    # else:
    #     template = 'registration/register.html'

    # return render(request, template, {})