import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from komponentkeeperapp.models import Component, Creator

@login_required
def components_list(request, pk=None):
    # Check if the request made is a GET request
    
    # get a reference to the logged in user 
    creatorId = Creator.objects.get(user_id=request.user.id)
    print('Creator ID', creatorId)
    if request.method == 'GET':
        pk = None
        # Assign all of the requested items to a variable
        # * all_components = Component.objects.all() 
        user_components = Component.objects.filter(creator=creatorId.id)
        # Then store each of the requested resource's values in a variable named after the keys in the model
        name = request.GET.get('name')
        # creator = request.GET.get('creator')
        # component.creator_id = creatorId.id
        image = request.GET.get('image')
        description = request.GET.get('description')
        
        template = 'components/list.html'
        context = {
            'user_components': user_components # * Changed
        }

        # return the render method passing in request, template and context as params
        return render(request, template, context)
        
        pass
    # elif request.method == 'POST':
    #     form_data = request.POST
        
    #     new_component = Component(
    #         creator_id = request.user.id,
    #         name = form_data['name'],
    #         image = upload_component(request),
    #         description = form_data['description']
    #     )

    #     print(new_component.name)
    #     new_component.save()
    #     return redirect(reverse('komponentkeeperapp:components'))