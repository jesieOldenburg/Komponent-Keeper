import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import Component
# from django.contrib.auth.decorators import login_required

def components_list(request):
    # Check if the request made is a GET request
    if request.method == 'GET':
        # Assign all of the requested items to a variable
        all_components = Component.objects.all()
        
        # Then store each of the requested resource's values in a variable named after the keys in the model
        creator = request.GET.get('creator')
        image = request.GET.get('image')
        description = request.GET.get('description')
        
        # TODO create a conditional statement to filter based on a not none condition that will reassign the value of all_components using all_components.filter(all_components__contains=creator) to filter based on creator
        
        # TODO assign the template path to the variable named template
        template = 'components/list.html'
        
        # TODO assign a value to the context dict i.e. 'all_components': all_components
        context = {
            'all_components': all_components
        }

        # return the render method passing in request, template and context as params
        return render(request, template, context)
        
        pass
    pass